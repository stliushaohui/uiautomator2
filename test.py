# -*- coding: utf-8 -*-
import uiautomator2 as u2
from time import sleep
from selenium import webdriver
from bn_test.lib.chromedriver import ChromeDriver
import atx
from atx.ext.chromedriver import ChromeDriver
# d = u2.connect_usb('P7CDU18402000714')
# d.app_start('com.fzsgbtb.bingniaozf')
# print('启动游戏')
# driver = ChromeDriver(d).driver()
# sleep(10)

import os
# os.environ['http_proxy'] = 'http://127.0.0.1:1080'
# os.environ['https_proxy'] = 'https://127.0.0.1:1080'

d = u2.connect()
d=u2.connect_usb('d9514a3c0804')
d.service("uiautomator").stop()
# d.app_start('com.tencent.mm')
# driver = ChromeDriver(d).driver()
# driver.find_element_by_id("index-kw").click()
# driver.find_element_by_id("index-kw").send_keys('python')
# driver.find_element_by_id("index-bn").click()
# print(driver.title)
# driver.quit()
# d(resourceId="com.tencent.mm:id/jc").click()
#
from bn_test.lib.bn_a2_lib import Bnautomator2
from atx.ext import chromedriver
# d = u2.connect_usb('P7CDU18402000714')
# d.app_clear('com.fzsgbtb.bingniaozf')
# d.app_start('com.fzsgbtb.bingniaozf')
# print('qidongyingyongle')
# # b = Bnautomator2()
# # d.d('com.android.packageinstaller:id/permission_allow_button').click()
# a = d(resourceId='com.android.packageinstaller:id/permission_allow_button')
# a.click()
# b.get_permission()

# driver = ChromeDriver(d).driver('192.168.31.15:5555')
# # print(driver.context)
# sleep(10)
# # driver.find_element_by_xpath('//*[@id="user-center"]/a[1]/div[1]/span[2]').click()
# sleep(2)
# driver.quit()\# driver.find_element_by_xpath('//*[@resource-iself.d="layout"]/anself.droiself.d.view.View[3]').send_keys('张三')
# class A():
#     def __init__(self):
#         self.a = int(15)
#     def cc(self):
#         self.b = self.a
#         print(self.b)
#     def b(self):
#         self.b = self.a
#         print(self.b)
# AA = A()
# AA.cc()


# import time
# import uiautomator2 as u2 #将chromedriver.py和该脚本放在同一目录下
#
# d1 = u2.connect_usb('P7CDU18402000714')
# d.app_start('com.github.android_app_bootstrap')
# d(text='Login').click()
# d(text='Baidu').click()
# time.sleep(3)
# print(d.info)
# # print(d.app_current.activity)
# # print(d.app_info())
# driver = ChromeDriver(d).driver()
# driver.find_element_by_id('index-kw').click()
# driver.find_element_by_id('index-kw').send_keys('Python')
# driver.find_element_by_id('index-bn').click()
# driver.quit()
# driver = ChromeDriver(d1).driver()
# driver.find_element_by_id("index-kw").click()
# driver.find_element_by_id("index-kw").send_keys('python')
# driver.find_element_by_id("index-bn").click()
# print(driver.title)
# # driver.quit()
# d1(resourceId="com.tencent.mm:id/jc").click()  #点击左上角的X

class An:
    def a(self,x):
        self.x = x
        print(self.x)
aaa = An()
aaa.a(15)


