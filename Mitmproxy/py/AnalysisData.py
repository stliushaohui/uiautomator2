import base64
import json
import os
import re
import urllib
from urllib import parse

import pbjson
import sys
from protobuf import bn_sdk_pb2
from protobuf import fx_sdk_pb2
from protobuf import qd_sdk_pb2

class AnalysisDataModle:
    def __init__(self):
        # 保存 分析结果 文件
        self.analysis_result_json_file = '../data/analysis_result_data.json'
        # 解析json数据
        # self.request_json_data = []
        # 配置文件 的接口列表
        # self.urlList = []
        self.code = 0
        self.mode = ''

        self.sdk_type = 'bn'
        self.bnLogList = {
            'start': bn_sdk_pb2.SDK3PushLogStart(), 'game': bn_sdk_pb2.SDK3PushLogGame(), 'roleup': bn_sdk_pb2.SDK3PushLogRoleUpdate(),
            'dur': bn_sdk_pb2.SDK3PushLogDur(), 'period': bn_sdk_pb2.SDK3PushLogPeriod(), 'xiadan': bn_sdk_pb2.SDK3PushLogXiadan()
        }
        self.fxLogList = {
            'start': fx_sdk_pb2.FxSDKPushLogStart(), 'enter': fx_sdk_pb2.FxSDKPushLogEnter(), 'game': fx_sdk_pb2.FxSDKPushLogGame(), 'role': fx_sdk_pb2.FxSDKPushLogRole(),
            'roleup': fx_sdk_pb2.FxSDKPushLogRoleUpdate(), 'dur': fx_sdk_pb2.FxSDKPushLogDur(), 'task': fx_sdk_pb2.FxSDKPushLogTask(), 'gold': fx_sdk_pb2.FxSDKPushLogGold()
        }
        self.logTypeList = {'bn':self.bnLogList, 'qd':'qd', 'fx':self.fxLogList}

        # 分析之前 先删除 旧的请求分析结果文件
        if os.path.exists(self.analysis_result_json_file) :
            os.remove(self.analysis_result_json_file)


    # 开始解析 API 数据
    def analysisApiData(self, sdk_type, json_data, config_data):
        urlList = []
        # 目前准备解析的 sdk 配置文件 类型 (bn、qd、fx、os)
        self.sdk_type = sdk_type
        # 先循环读取读取 配置文件 url 列表
        if not config_data is None:
            for i in range(len(config_data)) :
                urlList.append(config_data[i]['url'])

        if not (len(sys.argv) >= 2 and sys.argv[1] in 'input'):
            print('当前配置文件 Url : ' + str(urlList))

        if not json_data is None:
            # 循环 抓包数据 进行分析
            for i in range(len(json_data)) :
                code = json_data[i]['code']         # 接口返回码
                host = json_data[i]['host']         # 请求的 Host
                method = json_data[i]['method']     # 请求方式

                url = json_data[i]['url']           # 请求的 Url
                params = json_data[i]['params']     # 请求的参数
                responseData = json_data[i]['data'] # 接口返回参数

                # 判断 如果当前为 get 请求方式 则 在 url 里面 截取 请求参数 ? 后面
                if method == 'GET' :
                    urlStr = url.split('?', 1)
                    url = urlStr[0]
                    params = urlStr[1]

                print('\n---------------------------------- 解析数据 ----------------------------------')
                isUploadUrl = False # 是否为上报接口

                # 判断 当前抓包 url 存在于 配置文件
                if url in urlList:
                    # 获取 当前 url 在配置文件的位置
                    position = urlList.index(url)

                    # 判断 如果当前配置 是否不包含 isAnalysisParams 或 isAnalysisParams 为 true
                    # 是则 进行 参数解析 , 否则不解析 (上报接口 因为没有参数 而是直接 base64字符串 所以不能解析参数)
                    if not 'isAnalysisParams' in config_data[position] or config_data[position]['isAnalysisParams'] != False:
                        params = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url + '?' + params).query, True))

                    # 判断 当前 url 在配置文件里面 是否定义为 上报接口
                    if 'type' in config_data[position] and config_data[position]['type'] == 'tj_upload':
                        isUploadUrl = True

                    # 解析 请求参数
                    isSuccess = self.matchData(isUploadUrl, config_data[position], url, params, responseData, json_data[i])
                    if isSuccess :
                        print('当前 Url : ' + url + ' , 传递数据未发现异常')
                    else:
                        print('当前 Url : ' + url + ' , 传递数据异常')
                else:
                    print('当前 Url不存在于配置文件 : ' + url)
        else :
            print('数据为空')


    '''
    匹配数据
    is_upload_url : 是否为 上报接口
    config_data : 当前 url对应的 配置文件 json
    url : 解析的 url
    params : 解析的 请求参数
    response : 解析的 响应参数
    '''
    def matchData(self, is_upload_url, config_data, url, params, response, api_json_data):
        isSuccess = False

        aa = {'params' : {'success': ''}}

        c_url = config_data['url']            # 配置文件的 url
        c_request = []
        c_response = []
        if 'request' in config_data :
            c_request = config_data['request']    # 配置文件的 请求参数
        if 'response' in config_data :
            c_response = config_data['response']  # 配置文件的 响应参数
        if len(response) > 0 :
            response = eval(response.replace('true', 'True').replace('false', 'False'))
            if self.typeof(response) == 'str':
                response = eval(response)

        # 如果当前为 上报 url 则 进行 protobuf 解码 后再解析
        if is_upload_url:
            # 获取 当前上报类型
            urlList = url.split('/')
            name = urlList[len(urlList) - 1]
            # 判断 当前 上报 url 类型 是否存在 protobuf 文件里面
            if name in self.logTypeList[self.sdk_type] :
                b64_params = base64.b64decode(params)               # 先 base64 decode 原上报数据
                receiveData = self.logTypeList[self.sdk_type][name] # 获取 对应的 上报类型对象
                receiveData.ParseFromString(b64_params)             # protobuf 对象转 string 类型
                params = pbjson.pb2json(receiveData)                # protobuf 数据转 json 对象
                params = eval(params.replace('true', 'True'))       # python 不支持 小写 bool 类型 , 所以需要 替换成 大写
            else:
                print('当前上报类型 不存在 protobuf 里面 , type : ' + name)
                return isSuccess

        print('\n准备分析 url : ' + url)
        self.code = api_json_data['code']

        self.mode = 'request'
        requestList = self.startMatch(c_request, params)
        self.mode = 'response'
        responseList = self.startMatch(c_response, response)
        self.mode = ''



        print('1 请求成功的 Key : ' + str(requestList[0]))
        if not (len(sys.argv) >= 2 and sys.argv[1] in 'input'):
            print('1 响应成功的 Key : ' + str(responseList[0]) + '\n')

        print('2 请求失败的 Key : ' + str(requestList[1]))
        if not (len(sys.argv) >= 2 and sys.argv[1] in 'input'):
            print('2 响应失败的 Key : ' + str(responseList[1]) + '\n')

        print('3 请求警告的 Key : ' + str(requestList[2]))
        if not (len(sys.argv) >= 2 and sys.argv[1] in 'input'):
            print('3 响应警告的 Key : ' + str(responseList[2]) + '\n')

        print('4 请求错误的 Key : ' + str(requestList[3]))
        if not (len(sys.argv) >= 2 and sys.argv[1] in 'input'):
            print('4 响应错误的 Key : ' + str(responseList[3]))

        # 保存分析记录
        self.saveData(api_json_data['code'], api_json_data['method'], url, params, response, requestList, responseList)

        if len(requestList[1]) <= 0 and len(responseList[1]) <= 0 and len(requestList[3]) <= 0 and len(responseList[3]) <= 0 :
            isSuccess = True
        return isSuccess

    '''
    开始解析匹配 数据
    c_data : 配置数据 字典
    a_data : 原始数据 字典
    '''
    def startMatch(self, c_data, a_data):
        successKey = []
        failKey = []
        warningKey = []
        errorKey = []
        # 循环 请求参数 key
        for i in range(len(c_data)) :
            typeName = self.typeof(c_data[i])    # 先判断类型
            # 匹配普通 Key
            if typeName == 'list' or typeName == 'str':
                dataList = self.containsKey(a_data, c_data[i])
                successKey.extend(dataList[0])
                failKey.extend(dataList[1])
                warningKey.extend(dataList[2])
                errorKey.extend(dataList[3])
            # 匹配 传递的参数 的值 有多个参数的 json
            elif typeName == 'dict' :
                key = c_data[i]['key']
                valuesList = c_data[i]['values']

                try:
                    a_keyList = a_data[key]
                except Exception as e:
                    a_keyList = ''

                dataList = self.startMatch(valuesList, a_keyList)

                # if len(valuesList) > 1 and valuesList[1]:
                #     dataList = self.startMatch(valuesList, a_data[key])
                # else:
                #     # 匹配 json值格式的 全部值
                #     dataList = self.containsKey(a_data[key], valuesList)


                if len(dataList[0]) > 0 :
                    successJson = {'key':key,'values':dataList[0]}
                    successKey.append(successJson)
                if len(dataList[1]) > 0 :
                    failJson = {'key':key,'values':dataList[1]}
                    failKey.append(failJson)
                if len(dataList[2]) > 0 :
                    warningJson = {'key':key,'values':dataList[2]}
                    warningKey.append(warningJson)
                if len(dataList[3]) > 0 :
                    errorJson = {'key':key,'values':dataList[3]}
                    errorKey.append(errorJson)

        return [successKey, failKey, warningKey, errorKey]

    '''
    判断当前 数组里面的全部key 或 单个key 是否存在 某个字典中
    r_data : 原字典
    c_data : 数组 key 或 单个字符串 key
    return : 返回 不存在的 全部 Key 数组
    '''
    def containsKey(self, r_data, c_data):
        dataList = []
        successKey = []
        failKey = []
        warningKey = []
        errorKey = []
        typeName = self.typeof(c_data)
        if typeName == 'list' :
            # 由于嵌套在 key 里面的 json格式 值是字符串 , 所以需要转字典
            if self.typeof(r_data) == 'str':
                if not r_data is None and not r_data in '':
                    r_data = eval(r_data)
                else:
                    r_data = {}

            for key in c_data :
                self.matchKey(key, r_data, successKey, failKey, warningKey, errorKey)
                # keyList = str(key).split(';')
                #
                # # 需要修改为 有固定值 必须要对应固定值 , -1 表示可以不需要这个key 加到警告
                # isOptional = False  # 是否选填
                # isFixed = False     # 是否固定值
                # if len(keyList) >= 2 :
                #     if keyList[1] == '-1':
                #         isOptional = True
                #     else:
                #         isFixed = True
                #
                #
                # if keyList[0] in r_data.keys() :
                #     if isFixed :
                #         # 是 固定值 且 值相等 , 添加到 成功key
                #         if r_data[keyList[0]] == keyList[1] :
                #             successKey.append(keyList[0])
                #         else:
                #             # 否则 添加到 错误key = ret=0
                #             errorKey.append(key + ' = ' + r_data[keyList[0]])
                #     else:
                #         # 不是 固定值 直接 key 存在 就 添加到 成功key
                #         successKey.append(keyList[0])
                # else:
                #     # 不存在key 且 是选填值 则 直接添加到 警告key
                #     if isOptional :
                #         warningKey.append(keyList[0])
                #     else:
                #         # 否则 添加到 失败key
                #         failKey.append(keyList[0])

        elif typeName == 'str' :
            type = self.typeof(r_data)
            if type == 'list' :
                for i in range(len(r_data)) :
                    self.matchKey(c_data, r_data[i], successKey, failKey, warningKey, errorKey, position = '[' + str(i) + ']')
            else:
                self.matchKey(c_data, r_data, successKey, failKey, warningKey, errorKey)
            # if c_data in r_data :
            #     successKey.append(c_data)
            # else:
            #     failKey.append(c_data)

        dataList.append(successKey)
        dataList.append(failKey)
        dataList.append(warningKey)
        dataList.append(errorKey)
        return dataList

    '''
    匹配 Key 值
    key : 匹配的 key
    r_data : 原数据
    successKey : 保存成功 key 的数组
    failKey : 保存失败 key 的数组
    warningKey : 保存警告 key 的数组
    errorKey : 保存错误 key 的数组
    position : 位置 , 用于 数组 key 里面 排除当前key所在的数组位置
    '''
    def matchKey(self, key , r_data, successKey, failKey, warningKey, errorKey, position = ''):
        if self.typeof(r_data) == 'str':
            if not r_data is None and not r_data in '':
                r_data = eval(r_data)
            else:
                r_data = {}

        keyList = str(key).split(';')
        isOptional = False  # 是否选填
        isFixed = False     # 是否固定值
        if len(keyList) >= 2 :
            if keyList[1] == '-1':
                isOptional = True
            else:
                isFixed = True

        if keyList[0] == 'if_code':
            if keyList[1] == str(self.code):
                successKey.append('返回状态码' + position + ' = ' + str(self.code))
            else:
                warningKey.append('返回状态码' + position + ' = ' + str(self.code) + '(' + keyList[2] + ')')
            return

        if keyList[0] in r_data.keys():
            if isFixed :
                # 如果 是固定值 且 值为 需要判断大于 固定值
                if keyList[1].startswith('>'):
                    # 如果是大于 则 添加到成功 key = ret > 固定值
                    if r_data[keyList[0]] > int(keyList[1].replace('>', '')):
                        successKey.append(keyList[0]  + position + ' = ' + str(r_data[keyList[0]]) + ' ' + keyList[1])
                    else:
                        # 否则 添加到 错误 key = ret 不 > 固定值
                        errorKey.append(keyList[0]  + position + ' = ' + str(r_data[keyList[0]]) + ' 不 ' + keyList[1])
                    return

                # 是 固定值 且 值相等 , 添加到 成功key
                if r_data[keyList[0]] == keyList[1] :
                    successKey.append(keyList[0] + position)
                else:
                    # 否则 添加到 错误key = ret = 0
                    errorKey.append(keyList[0]  + position + ' = ' + r_data[keyList[0]])
            else:
                # 如果当前 Key 值 为 空字符串 或 null 则添加到 错误列表 , 只判断 分析请求参数的时候
                if (self.mode == 'request') and (self.typeof(r_data[keyList[0]]) == 'str') and (r_data[keyList[0]] is None or r_data[keyList[0]] in 'null' or r_data[keyList[0]] in ''):
                    # 是选填值 则 直接添加到 警告key
                    if isOptional :
                        warningKey.append(keyList[0] + position)
                    else:
                        # 否则 添加到 失败key
                        failKey.append(keyList[0] + position)
                    return

                # 不是 固定值 直接 key 存在 就 添加到 成功key
                successKey.append(keyList[0] + position)
        else:
            # 不存在key 且 是选填值 则 直接添加到 警告key
            if isOptional :
                warningKey.append(keyList[0] + position)
            else:
                # 否则 添加到 失败key
                failKey.append(keyList[0] + position)


    # 保存数据
    def saveData(self, code, method, url, params, response, requestList, responseList):
        json_list = self.getRequestJson(self.analysis_result_json_file)
        paramsKey = {'success' : requestList[0], 'fail' : requestList[1], 'warningKey' : requestList[2], 'errorKey' : requestList[3]}
        responseKey = {'success' : responseList[0], 'fail' : responseList[1], 'warningKey' : responseList[2], 'errorKey' : responseList[3]}

        request_dict = {
            'code': code,
            'method': method,
            'url': url,
            'params': params,
            'response': response,
            'result':{
                'paramsKey': paramsKey,
                'responseKey': responseKey
            }
        }

        json_list.append(request_dict)
        if not (len(sys.argv) >= 2 and sys.argv[1] in 'input'):
            with open(self.analysis_result_json_file, "w") as file:
                json.dump(json_list, file, sort_keys=True, indent=4, separators=(',', ': '))
                print("保存数据成功!")


    # 获取 本地保存起来的 抓包数据
    def getRequestJson(self, file):
        jsonData = []
        if os.path.exists(file) :
            with open(file, 'r', encoding='utf-8') as json_file:
                try:
                    json_text = ''
                    for line in json_file.readlines():
                        json_text += line
                    # 处理// ... /n 格式非json内容
                    json_str1 = re.sub(re.compile('(///\\s[\\s\\S]*?\n)'), '', json_text)
                    # 处理/*** ... */ 格式非json内容
                    # json_str2 = re.sub(re.compile('(/\*\*\*[\\s\\S]*?/)'), '', json_str1)
                    # print(json_str1)
                    jsonData = json.loads(json_str1)
                except Exception as e:
                    print('json 文件解析异常 , ' + str(e))
        return jsonData

    # 获取 变量的类型
    def typeof(self, variate):
        type1 = ""
        if type(variate) == type(1):
            type1 = "int"
        elif type(variate) == type("str"):
            type1 = "str"
        elif type(variate) == type(12.3):
            type1 = "float"
        elif type(variate) == type([1]):
            type1 = "list"
        elif type(variate) == type(()):
            type1 = "tuple"
        elif type(variate) == type({"key1":"123"}):
            type1 = "dict"
        elif type(variate) == type({"key1"}):
            type1 = "set"
        return type1

# -------------------------------------------------------------------------------------------------------------------- #