#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'minamoto'
__ver__ = '0.1'
__doc__ = 'slu handler'

import mxpsu as mx
import mxweb
from tornado import gen

import base
import pbiisi.msg_ws_pb2 as msgws
import utils


@mxweb.route()
class QueryDataMruHandler(base.RequestHandler):

    _help_doc = u'''电表数据查询 (post方式访问)<br/>
    <b>参数:</b><br/>
    &nbsp;&nbsp;uuid - 用户登录成功获得的uuid<br/>
    &nbsp;&nbsp;pb2 - rqQueryDataMru()结构序列化并经过base64编码后的字符串<br/>
    <b>返回:</b><br/>
    &nbsp;&nbsp;QueryDataMru()结构序列化并经过base64编码后的字符串'''

    @gen.coroutine
    def post(self):
        user_data, rqmsg, msg, user_uuid = self.check_arguments(msgws.rqQueryDataMru(),
                                                                msgws.QueryDataMru())

        if user_data is not None:
            if user_data['user_auth'] in utils._can_read:
                sdt, edt = self.process_input_date(rqmsg.dt_start, rqmsg.dt_end, to_chsarp=1)
                if sdt + edt > 0:
                    strdt = ' and a.date_create>={0} and a.date_create<={1}'.format(sdt, edt)
                else:
                    strdt = ''
                strsql = '''select a.rtu_id,a.date_create,a.date_type_code,a.mru_type_code,a.mru_data 
                from {0}_data.data_mru_record as a 
                where EXISTS 
                (select rtu_id,date_create from 
                (select rtu_id,max(date_create) as date_create from {0}_data.data_mru_record group by rtu_id) as t 
                where a.rtu_id=t.rtu_id and a.date_create=t.date_create) {1} order by a.rtu_id,a.date_create desc'''.format(
                    utils.m_jkdb_name, strdt)
                record_total, buffer_tag, paging_idx, paging_total, cur = self.mydata_collector(
                    strsql,
                    need_fetch=1,
                    buffer_tag=msg.head.paging_buffer_tag,
                    paging_idx=msg.head.paging_idx,
                    paging_num=msg.head.paging_num)
                if record_total is None:
                    msg.head.if_st = 45
                else:
                    msg.head.paging_record_total = record_total
                    msg.head.paging_buffer_tag = buffer_tag
                    msg.head.paging_idx = paging_idx
                    msg.head.paging_total = paging_total
                    for d in cur:
                        dv = msgws.QueryDataMru.DataMruView()
                        dv.dt_create = mx.switchStamp(int(d[1]))
                        dv.tml_id = int(d[0])
                        dv.date_type_code = int(d[2])
                        dv.mru_type_code = int(d[3])
                        dv.mru_data = float(d[4])
                        msg.data_mru_view.extend([dv])
                del cur, strsql

        self.write(mx.convertProtobuf(msg))
        self.finish()
        del msg, rqmsg, user_data


@mxweb.route()
class MruDataGetHandler(base.RequestHandler):

    _help_doc = u'''电表设备即时抄表 (post方式访问)<br/>
    <b>参数:</b><br/>
    &nbsp;&nbsp;uuid - 用户登录成功获得的uuid<br/>
    &nbsp;&nbsp;pb2 - rqErrInfo()结构序列化并经过base64编码后的字符串<br/>
    <b>返回:</b><br/>
    &nbsp;&nbsp;ErrInfo()结构序列化并经过base64编码后的字符串'''

    @gen.coroutine
    def post(self):
        user_data, rqmsg, msg, user_uuid = self.check_arguments(msgws.rqMruDataGet(), None)

        if user_data is not None:
            if user_data['user_auth'] in utils._can_read:
                # 验证用户可操作的设备id
                if 0 in user_data['area_r'] or user_data['is_buildin'] == 1:
                    rtu_ids = ','.join([str(a) for a in rqmsg.tml_id])
                else:
                    rtu_ids = ','.join([str(a)
                                        for a in self.check_tml_r(user_uuid, list(rqmsg.tml_id))])

                if len(rtu_ids) == 0:
                    msg.head.if_st = 46
                else:
                    strsql = '''select a.rtu_id,a.rtu_fid,
                    b.mru_addr_1,b.mru_addr_2,b.mru_addr_3,b.mru_addr_4,b.mru_addr_5,b.mru_addr_6 
                    from {0}.para_base_equipment as a left join {0}.para_mru as b 
                    on a.rtu_id in ({1})'''.format(utils.m_jkdb_name, rtu_ids)
                    record_total, buffer_tag, paging_idx, paging_total, cur = self.mydata_collector(
                        strsql,
                        need_fetch=1)
                    for d in cur:
                        if int(d[1]) > 0:
                            tra = 2
                        else:
                            tra = 1
                        tcsmsg = libiisi.initRtuJson(mod=2,
                                                     src=2,
                                                     ver=1,
                                                     tver=1,
                                                     tra=tra,
                                                     cmd='wlst.mru.9100',
                                                     ip=self.request.remote_ip,
                                                     port=0,
                                                     addr=self.get_phy_list(d[1])[0],
                                                     data=dict(addr1=int(d[2]),
                                                               addr2=int(d[3]),
                                                               addr3=int(d[4]),
                                                               addr4=int(d[5]),
                                                               addr5=int(d[6]),
                                                               addr6=int(d[7]),
                                                               ver=rqmsg.dev_ver,
                                                               type=rqmsg.data_mark,
                                                               date=rqmsg.dt_mark,
                                                               br=rqmsg.baud_rate))
                        libiisi.set_to_send(tcsmsg, 0, False)
                        libiisi.send_to_zmq_pub('tcs.req.wlst.mru.9100',
                                                json.dumps(tcsmsg,
                                                           separators=(',', ':')).lower())
            else:
                msg.head.if_st = 11

        self.write(mx.convertProtobuf(msg))
        self.finish()
        del msg, rqmsg, user_data, user_uuid
