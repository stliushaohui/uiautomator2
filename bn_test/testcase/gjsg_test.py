# -*- coding: utf-8 -*-
import os
import uiautomator2 as u2
from bn_test.lib.bn_a2_lib import Bnautomator2
from bn_test.lib.AndroidDriver import AndroidDriver
import shutil
import unittest
from bn_test.lib.chromedriver import ChromeDriver
from time import sleep
class GjsgTest(unittest.TestCase):
    def setUp(self):
        print("开始测试")
    def test_1_delete_screen(self):
        if os.path.exists('./sdk_screen_shots'):
            shutil.rmtree('./sdk_screen_shots')
    def test_2_sdk(self):
        b = Bnautomator2()
        #账号登录
        b.accout_login()
        b.token_login()
        b.xfc()
        b.layout()
        b.other_login()
        #账号注册
        b.account_register()
        b.xfc()
        b.layout()
        b.other_login()
        #忘记密码
        b.forget_password()
        b.xfc()
        b.layout()
        b.other_login()
        # 测试手机登录
        b.phone()
        d = u2.connect_usb(b.get_deviceid())
        d.service("uiautomator").stop()
        sleep(5)
        self.ad = AndroidDriver()
        self.ad.first()
        sleep(10)
        self.ad.xfc()
        self.ad.customer_service()
        self.ad.unbind_phone()
        self.ad.bind_phone()
        self.ad.lagout()
        self.ad.other_login()
        self.ad.quick_register()
        self.ad.xfc()
        self.ad.real_name()
        self.ad.change_password()
        self.ad.token_login()
        self.ad.next_time()
        self.ad.xfc()
        self.ad.forum()
    # def test_3_game(self):
    #     os.system('python ./bn_test/gjsg_aircase/gjsg.py')
