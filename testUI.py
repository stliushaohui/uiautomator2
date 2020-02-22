# -*- coding:utf-8 -*-

# import tkinter as tk

from tkinter import *
import os
import threading
import platform
import psutil
from bn_test import bn_sdk_run
from time import sleep

WORK_SPACE_PATH = os.getcwd()
NOW_PATH = ''
PACKAGE_NAME = ''

# 对应pid来杀进程
def processinfo(processName):
    pids = psutil.pids()
    for pid in pids:
        # print(pid)
        p = psutil.Process(pid)
        # print(p.name)
        if p.name() == processName:
            print(pid)
            return True  # 如果找到该进程则打印它的PID，返回true
    return False  # 没有找到该进程，返回false

def getEntryToTest():
    os.chdir('../../')
    PACKAGE_NAME = packageEntry.get()
    # print(PACKAGE_NAME)
    # os.system('python ./bn_sszg_test/bn_sdk_run.py '+PACKAGE_NAME)
    with open('bn_test\\file\\package.txt', 'w', encoding='utf-8') as f:
        f.write(PACKAGE_NAME)
    dict_gjsg = ['com.sgsjz.bingniaozf','com.bingniao.slzhs','com.jpxxl.bingniaozf','com.ibingniao.sdk','com.xsgmjl.bingniaozfyl','com.fzsgbtb.bingniaozf','com.rgbsg.bingniaozf']
    dict_bzsh = ['com.ygssb.bzsh.bn']
    if PACKAGE_NAME in dict_gjsg:
        bn_sdk_run.test_gjsg()
    if PACKAGE_NAME in dict_bzsh:
        sleep(5)
        # bn_sdk_run.test_bzsh()

    # bn_sdk_run.testRun()

def opendThreadToEntryToTest():
    THREAD_TEST = threading.Thread(target=getEntryToTest)
    THREAD_TEST.start()

# processinfo('你的文件名.py')
#D:/PycharmProjects/untitled
def runMitmproxy():
    NOW_PATH = os.getcwd()
    if(NOW_PATH!=WORK_SPACE_PATH):
        os.chdir(WORK_SPACE_PATH)
    os.chdir('./Mitmproxy/py')  # 切换工作目录
    os.system('mitmdump -p 8888 -s '+'./startMitmproxy.py')


def openThreadToAppuum():
    THREAD_APPIUM = threading.Thread(target=startAppium)
    THREAD_APPIUM.start()
def openThreadToUiautomator2():
    THREAD_APPIUM = threading.Thread(target=startUiatomator2)
    THREAD_APPIUM.start()

def openThreadToMitmproxy():
    DEF_THREAD = threading.Thread(target=runMitmproxy)
    DEF_THREAD.start()


def openThreadToStartTestRun():
    THREAD_START_TEST = threading.Thread(target=starTestRun)
    THREAD_START_TEST.start()


def startAppium():
    os.system('appium')  # 需要配环境变量
def startUiatomator2():
    os.system('python -m uiautomator2 init')

def endMitmproxy():
    if platform.system() == 'Windows':
        os.system('taskkill /IM mitmdump.exe /F')
        print('已经结束 mitmdump 进程')
        # endAppium()
        finishAppium()
        # processinfo('bn_sdk_run.py')
        print('已关闭测试脚本')
    else:
        # print('当前是其他操作系统：' + print(platform.system()) + ',请补全杀进程操作')
        print(processinfo('runMitmproxy.py'))

def finishAppium():
    if platform.system() == 'Windows':
        os.system('taskkill /IM Appium.exe /F')


def endAppium():
    if platform.system() == 'Windows':
        os.system('taskkill /f /fi "imagename eq node.exe"')
        print('已经结束 appium 进程')



def startCreateAnalysis():
    endMitmproxy()
    NOW_PATH = os.getcwd()
    if (NOW_PATH != WORK_SPACE_PATH):
        os.chdir(WORK_SPACE_PATH)
    os.chdir('./Mitmproxy/py')#切换工作目录
    os.system('python ./startAnalysisData.py')

def openThreadtoCreateAnalysis():
    THREAD_ANALYSIS = threading.Thread(target=startCreateAnalysis)
    THREAD_ANALYSIS.start()

def starTestRun():
    os.system('python ./bn_test/bn_sdk_run.py')


def starTestUIWeb():
    # NOW_PATH = os.getcwd()
    # if (NOW_PATH != WORK_SPACE_PATH):
    #     os.chdir(WORK_SPACE_PATH)
    os.chdir('../../')
    os.system('python ./loadJSONHead.py')
    finishApp()

openThreadToMitmproxy()
# 初始化TK界面
myWindow = Tk()
myWindow.title('Python Auto Test GUI')
myWindow.geometry('500x500')
def finishApp():
    # os.chdir('../../')
    endMitmproxy()
    endAppium()
    processinfo('testUI.py')
    start_dir = r''+PACKAGE_NAME
    os.startfile(start_dir)
    # os.system('start explorer '+PACKAGE_NAME)
    myWindow.destroy()

# button1 = Button(myWindow, text='开启抓包监听', command=openThreadToMitmproxy)
# button2 = Button(myWindow, text='关闭抓包监听', command=endMitmproxy)
button3 = Button(myWindow, text='开启Appium', command=openThreadToAppuum)
# button4 = Button(myWindow, text='关闭Appium', command=endAppium)
button4 = Button(myWindow, text='开启uiautomator2', command=openThreadToUiautomator2())
# button5 = Button(myWindow, text='输入包名点击测试', command=openThreadToStartTestRun)
button5 = Button(myWindow, text='输入包名点击测试', command=opendThreadToEntryToTest)
button6 = Button(myWindow, text='生成分析报告', command=startCreateAnalysis)
button7 = Button(myWindow, text='生成展示页mainTest.html', command=starTestUIWeb)
button8 = Button(myWindow, text='关闭', command=finishApp)
packageEntry = Entry(myWindow)
packageEntry.grid(row=3, column=2, padx=10, pady=10)




# button1.grid(row=1, column=1, padx=10, pady=10)
# button2.grid(row=1, column=2, padx=10, pady=10)
button3.grid(row=2, column=1, padx=10, pady=10)
button4.grid(row=2, column=2, padx=10, pady=10)
button5.grid(row=3, column=1, padx=10, pady=10)
button6.grid(row=4, column=1, padx=10, pady=10)
button7.grid(row=4, column=2, padx=10, pady=10)
# button8.grid(row=4, column=3, padx=10, pady=10)

myWindow.mainloop()
