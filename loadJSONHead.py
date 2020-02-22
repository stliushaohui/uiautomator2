# -*- coding:utf-8 -*-
import json
import time, datetime
import os



#计数器
COUNT_NUM = 0
#时间戳
TIME_STAMP = 0
#测试日期
TEST_TIME = ''
#游戏版本号、
GAME_VERSION = ''
#SDK版本号
SDK_VERSION = ''
#游戏类型（是否是冰鸟游戏）
GAME_TYPE = ''
#游戏ID
APP_ID = ''
#测试接口的HTML_注入字符串
STR_HTML = ''
#HTML 文件名字
HTML_NAME = 'mainTest.html'
#游戏截图目录
# IMG_FILE_PATH = './bn_sszg_test(1)/bn_sszg_test/screen_shots/'
IMG_FILE_PATH = './sdk_screen_shots/'
#html图片IMG标签
IMG_HTML = ''

#读分析后的JSON数据
with open("./Mitmproxy/data/analysis_result_data.json", 'r') as f:
    JSON_MAIN = json.loads(f.read())
    JSON_SIZE = len(JSON_MAIN)
    for interfaceJSON in JSON_MAIN:
        url = interfaceJSON['url']
        erTitleArray = []
        erContentArray = []
        wtTitleArray = []                                                                       # 匹配请求的警告弹框标题
        wtContentArray = []                                                                     #匹配请求的警告弹框内容
        if url == 'https://m.xiaotengyouxi.com/api/init':
            APP_ID = interfaceJSON['params']['app_id']
            GAME_VERSION = interfaceJSON['params']['game_version']
            SDK_VERSION = interfaceJSON['params']['sdk_version']
            appId = interfaceJSON['params']['app_id']
            # appId = 'q123'
            if appId.isnumeric():
                #是纯数字 代表 冰鸟
                print('纯数字')
                GAME_TYPE = '该游戏是冰鸟游戏'
            else:
                #非纯数字
                if appId in '_':
                    #里面包含下划线 代表鹰魂
                    print('有下划线')
                    GAME_TYPE = '该游戏是鹰魂游戏'
                else:
                    if appId.startswith('q'):
                        #是q开头 但里面没有下划线(代表轻度)
                        print('q开头但没有下划线')
                        GAME_TYPE = '该游戏是轻度游戏'
            TIME_STAMP = int(interfaceJSON['params']['time'])
            timeArray = time.localtime(TIME_STAMP)
            TEST_TIME = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        showSuccess = ''
        showFail = ''
        showWT = ''
        paramsData = interfaceJSON['params']                                                    #请求数据
        # print(str(paramsData))
        responesData = interfaceJSON['response']                                                #返回数据
        resultData = interfaceJSON['result']                                                    #分析的结果数据
        paramsyKeyData = interfaceJSON['result']['paramsKey']                                   #分析请求数据
        sponesKeyData = interfaceJSON['result']['responseKey']                                  #分析响应数据

        paramsySuccesResultData = interfaceJSON['result']['paramsKey']['success']               #分析后成功的请求数据
        paramsyErrorResultData = interfaceJSON['result']['paramsKey']['errorKey']               #分析后错误的请求数据
        paramsyFailResultData = interfaceJSON['result']['paramsKey']['fail']                    #分析后失败的请求数据
        paramsyWarningResultData = interfaceJSON['result']['paramsKey']['warningKey']           #分析后警告的请求数据

        spSuccessResultData = interfaceJSON['result']['responseKey']['success']                 #分析后成功的返回数据
        spFaileResultData = interfaceJSON['result']['responseKey']['fail']                      #分析后失败的返回数据
        spErrorResultData = interfaceJSON['result']['responseKey']['errorKey']                  #分析后错误的返回数据
        spWarningResultData = interfaceJSON['result']['responseKey']['warningKey']              #分析后警告的返回数据
        if len(paramsyErrorResultData) == 0 and len(paramsyFailResultData) == 0 and len(paramsyWarningResultData) == 0 \
                and len(spFaileResultData) == 0 and len(spErrorResultData) == 0 and len(spWarningResultData) == 0:
            showSuccess = 'inline'
            showFail = 'none'
            showWT = 'none'
        else:
            showSuccess = 'none'
            if len(paramsyErrorResultData) != 0 or len(paramsyFailResultData) != 0 or len(spFaileResultData) != 0 or\
                    len(spErrorResultData) != 0:
                showFail = 'inline'
                if len(paramsyErrorResultData) != 0:
                    erTitleArray.append("匹配请求错误详情")
                    erContentArray.append(paramsyErrorResultData)
                if len(paramsyFailResultData) != 0:
                    erTitleArray.append("匹配请求失败详情")
                    erContentArray.append(paramsyFailResultData)
                if len(spFaileResultData) != 0:
                    erTitleArray.append("匹配返回失败详情")
                    erContentArray.append(spFaileResultData)
                if len(spErrorResultData) != 0:
                    erTitleArray.append("匹配返回错误详情")
                    erContentArray.append(spErrorResultData)
            else:
                showFail = 'none'
            if len(paramsyWarningResultData) != 0 or len(spWarningResultData) != 0:
                showWT = 'inline'
                if len(paramsyWarningResultData) != 0:
                    wtTitleArray.append("匹配请求警告详情")
                    wtContentArray.append(paramsyWarningResultData)
                if len(spWarningResultData)!= 0:
                    wtTitleArray.append("匹配返回警告详情")
                    wtContentArray.append(spWarningResultData)
            else:
                showWT = 'none'
        STR_HTML += "<div class='panel panel-default'><div class='panel-heading' role='tab' id='headingOne"+str(COUNT_NUM)+"'>\
        <h4 class='panel-title'><a id='test_url"+str(COUNT_NUM)+"' \
        role='button' data-toggle='collapse' data-parent='#accordion' href='#collapseOne"+str(COUNT_NUM)+"' \
        aria-expanded='false' aria-controls='collapseOne'>测试的接口:"+url+"\
        </a><div style='float: right;'><strong id='ifsSuccess' style='color: green;display:"+showSuccess+";'> 成功</strong>\
        <strong id='ifsFail' data-tag = '"+"showDialog2"+"' data-titlejson='"+json.dumps(erTitleArray)+"' \
        data-contentjson='"+json.dumps(erContentArray)+"' \
        style='color:red;display:"+showFail+";'> 失败</strong>\
        <strong id='ifsWT' data-tag = '"+"showDialog2"+"' data-titlejson = '"+json.dumps(wtTitleArray)+"' \
        data-contentjson = '"+json.dumps(wtContentArray)+"' \
        style='color: orange;display:"+showWT+";'> 警告</strong>\
        </div></h4></div><div id='collapseOne"+str(COUNT_NUM)+"' class='panel-collapse collapse' role='tabpanel' \
        aria-labelledby='headingOne'><div class='panel-body'><table class='table table-bordered'><thead><tr class='table1'>\
        <th width='50%'>请求数据</th><th width='50%'>返回数据</th></tr></thead>\
        <tbody><tr><td  width='50%'><a id = 'request_ditail"+str(COUNT_NUM)+"' \
        data-title = '请求数据详情' data-val = '"+str(json.dumps(paramsData))+"' >请求数据详情</a></td>\
        <td width='50%'><a id = 'response_ditail"+str(COUNT_NUM)+"' \
        data-title = '返回数据详情' data-val = '"+str(json.dumps(responesData))+"'>返回数据详情</a></td></tr></tbody>\
        </table><table class='table table-bordered'><tr><td><a id='request_success_ditail"+str(COUNT_NUM)+"' \
        data-title = '匹配请求成功详情' data-val = '"+str(json.dumps(paramsySuccesResultData))+"'>匹配\
        请求成功详情</a></td><td><a id='request_fail_ditail"+str(COUNT_NUM)+"' data-title = '匹配请求失败详情' \
        data-val = '"+str(json.dumps(paramsyFailResultData))+"'>匹配请求失败详情</a></td><td>\
        <a id='request_warning_ditail"+str(COUNT_NUM)+"' data-title = '匹配请求警告详情' data-val = '"+str(json.dumps(paramsyWarningResultData))+"'>\
        匹配请求警告详情</a></td><td><a id='request_error_ditail"+str(COUNT_NUM)+"' data-title = '匹配请求错误详情' \
        data-val = '"+str(json.dumps(paramsyErrorResultData))+"'>匹配请求错误详情</a></td></tr>\
        </table><table class='table table-bordered'><tr><td><a id='response_success_ditail"+str(COUNT_NUM)+"' \
        data-title = '匹配返回成功详情' data-val = '"+str(json.dumps(spSuccessResultData))+"'>匹配返回成功详情</a></td><td>\
        <a id='response_fail_ditail"+str(COUNT_NUM)+"' data-title = '匹配返回失败详情' data-val = '"+str(json.dumps(spFaileResultData))+"'>\
        匹配返回失败详情</a></td><td><a id='response_warning_ditail"+str(COUNT_NUM)+"' data-title = '匹配返回警告详情' data-val \
        = '"+str(json.dumps(spWarningResultData))+"'>匹配返回警告详情</a></td><td><a id='response_error_ditail"+str(COUNT_NUM)+"' \
        data-title = '匹配返回错误详情' data-val = '"+str(json.dumps(spErrorResultData))+"'>匹配返回错误详情</a></td></tr>\
        </table></div></div></div>"
        COUNT_NUM += 1

#读图片目录

for root, dirs, files in os.walk(IMG_FILE_PATH):
    # print('root:', root)      # 当前目录路径
    # print('dirs:', dirs)      # 当前路径下所有子目录
    # print('files:', files)    # 当前路径下所有非目录子文件
    files.sort()

    if len(files) != 0:
        b = 0
        a = 0
        c = 0
        d = 0
        for file in files:
            # 读取SDK自动化测试前六张图
            if file.split('.')[1] == 'png':
                if a > 100:
                    break
                IMG_HTML += "<img width='33%' src='" + root + file + "'>"
            a += 1
            # #读取游戏自动化测试前六张图
            # if file.split('.')[1] == 'jpg':
            #     if b > 5:
            #         break
            #     IMG_HTML += "<img width='33%' src='" + root + file + "'>"
            # b += 1
        for file in reversed(files):
            # #读取SDK自动化测试后六张图
            # if file.split('.')[1] == 'png':
            #     if c > 5:
            #         break
            #     IMG_HTML += "<img width='33%' src='"+root+file+"'>"
            # c += 1
            #读取游戏自动化测试后六张图
            if file.split('.')[1] == 'jpg':
                if d > 5:
                    break
                IMG_HTML += "<img width='33%' src='" + root + file + "'>"
            d +=1

#
# #改html文件
f = open('./index_result.html', 'r', encoding='utf-8')
# 把文件内容转化为字符串
f = f.read()
f = f.replace("&gameversion&", GAME_VERSION)
f = f.replace("&sdkversion&", SDK_VERSION)
f = f.replace("&timeStamp&", TEST_TIME)
f = f.replace("&appId&", "AppId:"+APP_ID)
f = f.replace("&testInterface&", STR_HTML)
f = f.replace("&img&", IMG_HTML)
f = f.replace("&isBn&", GAME_TYPE)
#生成新的html
file = open(HTML_NAME, 'w', encoding='utf-8')
file.write(f)
file.close()
print('生成完毕')






