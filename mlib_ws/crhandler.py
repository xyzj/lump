#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import base64
from pymxlib import SCRIPT_DIR
import tornado.web
import tornado.template
import tornado.websocket
from mlibws.pb2.chatroom_pb2 import chatmsg
from .wsutils import send_to_allws


log_chatroom = None
online_user = []
legal_users = {
    "19517e6a43e3c76ced8e3c9ec6447b4f": "minamoto",
    "0e12c88a6193cb05554848759149e219": "131",
    "7a0bd620f491c9b0fe7cbfc8ffa69e93": "lf",
    "": "lp",
    "ca4bfd7e8859ca458a3e2d0d5a0def2b": "jeffrey",
    "571aeabb5e73e32b9ad4f2d68a6777c4": "hsu",
    "70a9fbbce9d9e9eba70a972af51d6a4c": "admin",
}
# wsclients = []


class Index(tornado.web.RequestHandler):
    def get(self):
        try:
            # self.render("index.html")
            self.render(os.path.join(
                SCRIPT_DIR, "..", "chatroom", "index.html"))
        except Exception as ex:
            print(ex.message)


class ChatroomHandler(tornado.websocket.WebSocketHandler):
    # user = ""
    # uname = ""

    def __init__(self, application, request, **kwargs):
        global log_chatroom
        tornado.websocket.WebSocketHandler.__init__(
            self, application, request, **kwargs)
        self.legal = False
        log_chatroom = MyLogger("ws.chatroom", int(ConfData[
            "filelog_level"]), int(ConfData["consolelog_level"]))
        self.uname = ""
        # if not client_started:
        # cli = Client_to_server(ConfData[
        #                            "server_ip"], ConfData["server_port"])
        #     cli.setDaemon(True)
        #     cli.start()
        # print("chatroom")

    # @staticmethod
    # def send_to_allws(message, binary=False):
    # for client in wsclients:
    #         if client.legal == True:
    #             client.write_message(message, binary)

    # @staticmethod
    def make_error_message(self, reason):
        cr = chatmsg()
        cr.cr.type = "error"
        cr.cr.msg = reason
        return cr.SerializeToString()
        # error = dict()
        # error['type'] = 'error'
        # error['reason'] = reason
        # return json.dumps(error)

    # @staticmethod
    def make_success_message(self, data_type):
        cr = chatmsg()
        cr.cr.type = data_type
        cr.cr.uname = self.uname
        cr.cr.msg = "success"
        return cr.SerializeToString()
        # msg = dict()
        # msg['type'] = data_type
        # msg['status'] = 'success'
        # return json.dumps(msg)

    def open(self):
        global wsclients
        wsclients.append(self)

    def write_message(self, message, binary=False):
        try:
            message = base64.b64encode(message)
            tornado.websocket.WebSocketHandler.write_message(
                self, message, binary)
            log_chatroom.savelog("send:{0:s}".format(message), 20)
        except:
            self.on_close()

    def on_message(self, message):
        log_chatroom.savelog("rec:{0:s}".format(message), 20)
        message = base64.b64decode(message)
        log_chatroom.savelog("decode:{0:s}".format(message), 20)
        try:
            data = chatmsg()
            data.ParseFromString(message)
        except:
            self.write_message(self.make_error_message('badjson'))
            return

        data_type = data.cr.type
        if data_type == "login":
            self.legal = False
            self.activecode = data.cr.activecode
            user = legal_users.get(hashMD5(self.activecode))
            if user is None or user == "":
                self.write_message(
                    self.make_error_message('badlogin'))
                return
            if user in online_user:
                self.write_message(
                    self.make_error_message('alreadylogin'))
                return
            online_user.append(user)
            self.legal = True
            self.uname = user
            self.write_message(self.make_success_message("login"))
            cr = chatmsg()
            cr.cr.type = "member"
            cr.cr.memlist.extend(online_user)
            cr.cr.memlist.extend(["x1", "x2", "x3"])
            send_to_allws(cr.SerializeToString())
            return
        elif data_type == "logout":
            online_user.remove(self.uname)
            self.uname = ""
            self.write_message(self.make_success_message('logout'))
            cr = chatmsg()
            cr.cr.type = "member"
            cr.cr.memlist.extend(online_user)
            send_to_allws(cr.SerializeToString())
            return
        elif data_type == "newmsg":
            content = data.msg
            if content == "":
                self.write_message(
                    self.make_error_message('badmsg'))
                return
            self.write_message(self.make_success_message('send'))
            content = content.replace('<', '&lt;')
            content = content.replace('>', '&gt;')
            content = content.replace('\n', '<br>')
            cr = chatmsg()
            cr.cr.msg = content
            cr.cr.uname = self.uname
            cr.cr.activecode = self.activecode
            cr.cr.type = "newmsg"
            cr.cr.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            send_to_allws(cr.SerializeToString())
            return

    def on_close(self):
        global wsclients
        wsclients.remove(self)
        if self.uname == "":
            return
        online_user.remove(self.uname)
        self.uname = ""
        cr = chatmsg()
        cr.cr.type = "member"
        cr.cr.memlist.extend(online_user)
        send_to_allws(cr.SerializeToString())
        # send_to_all(base64.b64encode(cr.SerializeToString()))
