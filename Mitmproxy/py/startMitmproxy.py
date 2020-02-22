# -*- coding: utf-8 -*-
import urllib
from urllib import parse

import json
import os
from mitmproxy import ctx

import collections
import random

from enum import Enum

import mitmproxy
from mitmproxy.exceptions import TlsProtocolException
from mitmproxy.proxy.protocol import TlsLayer, RawTCPLayer

# mitmdump -p 8800 -s startMitmproxy.py

class Counter:
    def __init__(self):
        # 抓包的 hosts 配置路径
        self.host_file = '../data/config/host_config_data.json'
        # 保存 抓包结果的 文件路径
        self.json_file = '../data/request_data.json'
        self.url = ''   # 当前请求的 链接
        self.host = ''  # 当前请求的 Host
        self.method = ''# 当前请求的 方式
        self.params = ''# 当前请求的 传递参数

        self.code = 0   # 当前请求的 返回码
        self.data = ''  # 当前请求的 返回值
        self.path = ''  # 当前链接 对应的 Path 部分(用于判断链接后缀)

        # 抓包的时候 排除掉 这些后缀的文件不保存
        self.suffix = [
            'jpg'   , 'png' , 'js'  , 'html', 'css', 'ico',
            'exe'   , 'pdf' , 'swf' , 'apk' ,
            'gz'    , 'tgz' , 'tbz' , 'zip' , 'rar' , 'tar', '7z',
            'mp3'   , 'ogg' , 'mp4a', 'wav' , 'wma' ,
            'mp4'   , 'avi' , 'flv' , 'mkv'
        ]

        # 抓包之前 先删除 旧的请求数据文件
        if os.path.exists(self.json_file) :
            os.remove(self.json_file)

#----------------------------------------------------------------------------------------------------------------------#

    # 所有发出的请求数据包都会被这个方法所处理
    # 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
    def request(self, flow):
        # 获取请求对象
        request = flow.request
        # 实例化输出类
        info = ctx.log.info
        self.url = request.url
        self.host = request.host
        self.method = request.method
        self.params = str(request.text)

        self.path = urllib.parse.urlsplit(self.url).path
        # print('请求Url : ' + request.url)
        # 打印host头
        # info(request.host)
        # 打印请求端口
        # info(str(request.port))
        # 打印所有请求头部
        # info(str(request.headers))
        # 打印cookie头
        # info(str(request.cookies))

#----------------------------------------------------------------------------------------------------------------------#

    # 所有服务器响应的数据包都会被这个方法处理
    # 所谓的处理，我们这里只是打印一下一些项
    def response(self, flow):
        # 获取响应对象
        self.res = flow.response
        # 实例化输出类
        info = ctx.log.info
        # 响应码
        self.code = str(self.res.status_code)
        # 响应报文内容
        self.data = str(self.res.text)
        if self.host in self.getHostList() :
            # 判断 当前 链接 是否 包含某些 后缀 , 视为 文件 , 这种链接 不进行保存
            pathList = self.path.split('.')
            if not pathList[len(pathList) - 1] in self.suffix:
                self.saveRequestJson()
        # 打印所有头部
        # info(str(response.headers))
        # 打印cookie头部
        # info(str(response.cookies))

#----------------------------------------------------------------------------------------------------------------------#

    # 获取 符合条件的 Host 接口 列表
    def getHostList(self):
        host_file = []
        if os.path.exists(self.host_file) :
            with open(self.host_file, 'r') as host_file:
                try:
                    host_file = json.load(host_file)
                except Exception as e:
                    print('json 文件解析异常 , ' + str(e))
        return host_file

#----------------------------------------------------------------------------------------------------------------------#

    # 获取 本地保存的请求数据
    def getRequestJson(self):
        json_text = []
        if os.path.exists(self.json_file) :
            with open(self.json_file, 'r') as json_file:
                try:
                    json_text = json.load(json_file)
                except Exception as e:
                    print('json 文件解析异常 , ' + str(e))
        return json_text

#----------------------------------------------------------------------------------------------------------------------#

    # 保存请求数据到本地
    def saveRequestJson(self):
        json_list = self.getRequestJson()

        # 排除 Html 的 返回内容
        if '<!DOCTYPE html>' in self.data:
            self.data = ''

        # 请求 URL、请求方式、请求参数、返回码、返回数据
        request_dict = {'url': self.url, 'host': self.host, 'method': self.method, 'params': self.params, 'code': str(self.code), 'data': self.data}
        # request_dict = {'a':'a','b':'b','c':'c'}
        json_list.append(request_dict)
        with open(self.json_file, "w") as file:
            json.dump(json_list, file, sort_keys=True, indent=4, separators=(',', ': '))
            print(json_list)
            print("保存数据成功!")

#----------------------------------------------------------------------------------------------------------------------#

addons = [
    Counter()
]


class InterceptionResult(Enum):
    success = True
    failure = False
    skipped = None


class _TlsStrategy:
    """
    Abstract base class for interception strategies.
    """

    def __init__(self):
        # A server_address -> interception results mapping
        self.history = collections.defaultdict(lambda: collections.deque(maxlen=200))

    def should_intercept(self, server_address):
        """
        Returns:
            True, if we should attempt to intercept the connection.
            False, if we want to employ pass-through instead.
        """
        raise NotImplementedError()

    def record_success(self, server_address):
        self.history[server_address].append(InterceptionResult.success)

    def record_failure(self, server_address):
        self.history[server_address].append(InterceptionResult.failure)

    def record_skipped(self, server_address):
        self.history[server_address].append(InterceptionResult.skipped)


class ConservativeStrategy(_TlsStrategy):
    """
    Conservative Interception Strategy - only intercept if there haven't been any failed attempts
    in the history.
    """

    def should_intercept(self, server_address):
        if InterceptionResult.failure in self.history[server_address]:
            return False
        return True


class ProbabilisticStrategy(_TlsStrategy):
    """
    Fixed probability that we intercept a given connection.
    """

    def __init__(self, p):
        self.p = p
        super(ProbabilisticStrategy, self).__init__()

    def should_intercept(self, server_address):
        return random.uniform(0, 1) < self.p


class TlsFeedback(TlsLayer):
    """
    Monkey-patch _establish_tls_with_client to get feedback if TLS could be established
    successfully on the client connection (which may fail due to cert pinning).
    """

    def _establish_tls_with_client(self):
        server_address = self.server_conn.address

        try:
            super(TlsFeedback, self)._establish_tls_with_client()
        except TlsProtocolException as e:
            tls_strategy.record_failure(server_address)
            raise e
        else:
            tls_strategy.record_success(server_address)


# inline script hooks below.

tls_strategy = None


def load(l):
    l.add_option(
        "tlsstrat", int, 0, "TLS passthrough strategy (0-100)",
    )


def configure(updated):
    global tls_strategy
    if ctx.options.tlsstrat > 0:
        tls_strategy = ProbabilisticStrategy(float(ctx.options.tlsstrat) / 100.0)
    else:
        tls_strategy = ConservativeStrategy()


def next_layer(next_layer):
    """
    This hook does the actual magic - if the next layer is planned to be a TLS layer,
    we check if we want to enter pass-through mode instead.
    """
    if isinstance(next_layer, TlsLayer) and next_layer._client_tls:
        server_address = next_layer.server_conn.address

        if tls_strategy.should_intercept(server_address):
            # We try to intercept.
            # Monkey-Patch the layer to get feedback from the TLSLayer if interception worked.
            next_layer.__class__ = TlsFeedback
        else:
            # We don't intercept - reply with a pass-through layer and add a "skipped" entry.
            mitmproxy.ctx.log("TLS passthrough for %s" % repr(next_layer.server_conn.address), "info")
            next_layer_replacement = RawTCPLayer(next_layer.ctx, ignore=True)
            next_layer.reply.send(next_layer_replacement)
            tls_strategy.record_skipped(server_address)