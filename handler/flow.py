# -*- coding: utf-8 -*-

__author__ = 'minamoto'
__ver__ = '0.1'
__doc__ = 'rtu handler'

import xml.dom.minidom as xmld
from urllib import urlencode

import mxweb
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

import base
import utils


@mxweb.route()
class FlowWorkHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()
    root_path = r'/flow/'

    @gen.coroutine
    def get(self):
        url = '{0}/{1}'.format(utils.m_fs_url, self.request.uri.replace(self.root_path, ''))
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}/{1}'.format(utils.m_fs_url, self.request.uri.replace(self.root_path, ''))
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data

@mxweb.route()
class mobileLoginHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class getAssetHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data

@mxweb.route()
class getInfoHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data

@mxweb.route()
class getVersionHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class getFormHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class setGpsHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class getFilterBoxHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class listRecordHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class listTaskHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class listTaskRecordHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class listTaskAllHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class listDoneHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class getFormHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class getLogHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class doFetchHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class doTransitionHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data


@mxweb.route()
class GetDictValuesWithFilterHandler(base.RequestHandler):

    help_doc = u'''工作流接口封装 (get/post方式访问)<br/>
    <b>参数:</b></br>
    &nbsp;&nbsp;参考工作流相关文档'''

    keep_name_case = True
    thc = AsyncHTTPClient()

    @gen.coroutine
    def get(self):
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET', url, fields={}, timeout=7.0, retries=False)

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url

    @gen.coroutine
    def post(self):
        x = self.request.arguments
        data = dict()
        for k in x.keys():
            data[k] = x.get(k)[0]
        url = '{0}{1}'.format(utils.m_fs_url, self.request.uri)
        try:
            # rep = utils.m_httpclinet_pool.request('GET',
            #                                       url,
            #                                       fields=data,
            #                                       timeout=7.0,
            #                                       retries=False)
            url += '?{0}'.format(urlencode(data))

            rep = yield self.thc.fetch(url, raise_error=True, request_timeout=12)
            self.write(rep.body)
        except Exception as ex:
            self.write(str(ex))
        self.finish()
        del url, x, data
