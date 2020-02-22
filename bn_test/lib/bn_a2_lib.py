# -*- coding: utf-8 -*-
import uiautomator2 as u2
import os
import re
import time
from time import sleep
import random
from bn_test.lib.chromedriver import ChromeDriver
class Bnautomator2(object):
    # 获取设备多台设备号列表
    def __init__(self):
        with open('bn_test\\file\\package.txt') as f:
            self.ap = f.read()
    @staticmethod
    def get_deviceid():
        str_init = ' '
        all_info = os.popen('adb devices').readlines()
        for i in range(len(all_info)):
            str_init += all_info[i]
        devices_name = re.findall('\n(.+?)\t', str_init, re.S)
        return devices_name[0]
    #快速注册
    def quick_register(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.d(description="快速游戏").click()
        sleep(2)
        self.screenshot()
    #手机登录
    def phone(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d(description="手机登录").click()
        sleep(2)
        self.screenshot()
        self.d(resourceId=self.ap+":id/bn_edt_phone").click()
        self.d.send_keys("18024179019", clear=True)
        self.d(resourceId=self.ap+":id/bn_btn_next").click()
        path = '//*[@resource-id="'+self.ap+':id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
        self.d.xpath(path).click()
        self.d.send_keys("000000", clear=True)
        self.screenshot()
        self.d(resourceId=self.ap+":id/bn_btn_login").click()
    #账号登录
    def accout_login(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_clear(self.ap)
        self.d.app_start(self.ap)
        self.get_permission()
        sleep(5)
        self.d.app_stop(self.ap)
        self.d.app_start(self.ap)
        self.get_permission()
        sleep(5)
        self.d(description="账号登录").click()
        self.screenshot()
        self.d.xpath(
            '//*[@resource-id="'+self.ap+':id/bn_vp_content"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        self.d.send_keys("lshbnbn", clear=True)
        self.screenshot()
        self.d.xpath(
            '//*[@resource-id="'+self.ap+':id/bn_vp_content"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]').click()
        self.d.send_keys("123456", clear=True)
        self.screenshot()
        self.d(resourceId=self.ap+":id/yh_btn_sure").click()
    #账号注册
    def account_register(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.d(description="账号登录").click()
        self.d(text="账号注册").click()
        self.screenshot()
        self.d.xpath(
            '//*[@resource-id="'+self.ap+':id/bn_vp_content"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        username = 'bnuser' + str(random.randint(1000, 10000000))
        self.d.send_keys(username, clear=True)
        self.screenshot()
        self.d.xpath(
            '//*[@resource-id="'+self.ap+':id/bn_vp_content"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]').click()
        self.d.send_keys('bn123456', clear=True)
        self.screenshot()
        self.d(resourceId=self.ap+":id/yh_btn_sure").click()
    # 忘记密码
    def forget_password(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.d(description="账号登录").click()
        self.d(resourceId=self.ap+":id/bn_tv_forget").click()
        self.screenshot()
        self.d(resourceId=self.ap+":id/bn_rl_phone").click()
        self.d.send_keys("18024179019", clear=True)
        self.screenshot()
        self.d(resourceId=self.ap+":id/bn_btn_verify").click()
        self.d(resourceId=self.ap+":id/bn_edt_verify").click()
        self.d.send_keys("000000", clear=True)
        self.screenshot()
        self.d(resourceId=self.ap+":id/bn_rl_password").click()
        self.d.send_keys("123456", clear=True)
        self.screenshot()
        self.d(resourceId=self.ap+":id/bn_btn_login").click()
        # sleep(10)
        # self.d.click(0.019, 0.53)
        # self.d(text="退出登录").click()
    def screenshot(self):
        self.d = u2.connect_usb(self.get_deviceid())
        if not os.path.exists("./sdk_screen_shots"):
            # 判断截图目录是否存在，不存在则创建
            os.makedirs("./sdk_screen_shots")
        gamename = self.ap.split('.')[-1]
        path = './sdk_screen_shots/' + gamename + '_%s.png' % time.strftime("%Y-%m-%d %H-%M-%S")
        # path = './sdk_screen_shots/' + 'gjsg' + '_%s.png' % time.strftime("%Y-%m-%d %H-%M-%S")
        self.d.screenshot(path)
        if os.path.exists(path):
            return path
        else:
            return False

    # 获取权限按钮
    def get_permission(self):
        # self.d =u2.connect_usb(self.get_deviceid())
        time.sleep(3)
        while True:
            if self.is_element_appearance('com.android.packageinstaller:id/permission_allow_button') == True:
                time.sleep(2)
                # self.screenshot()
                sleep(2)
                self.d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
            else:
                break
    #绑定手机的下次再说按钮
    def next_time(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.d(resourceId=self.ap+":id/yh_btn_left").click()
    #token登录
    def token_login(self):
        # sleep(10)
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        # while True:
        #     sleep(3)
        #     if self.is_element_appearance(self.ap+":id/bn_btn_login")==True:
        self.d(resourceId=self.ap+":id/bn_btn_login").click()
            # else:
            #     break
    #点击悬浮窗按钮
    def xfc(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        sleep(10)
        self.screenshot()
        self.d.click(0.019, 0.53)
    #点击其他登录按钮
    def other_login(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        # while True:
        #     if self.is_element_appearance(self.ap + ":id/bn_tv_other")==True:
        self.d(resourceId=self.ap + ":id/bn_tv_other").click()
            # else:
            #     break
    def layout(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.d(text="退出登录").click()
    # H5个人中心，实名认证功能
    def real_name(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.driver = ChromeDriver(self.d).driver()
        self.driver.find_element_by_xpath()
        self.d(text="实名认证 未实名").click()
        self.d.xpath('//*[@resource-iself.d="layout"]/anself.droiself.d.view.View[3]').click()
        self.d.senself.d_keys("张三", clear=True)
        self.d.xpath('//*[@resource-iself.d="layout"]/anself.droiself.d.view.View[4]').click()
        self.d.senself.d_keys("440514199708087833", clear=True)
        pass
    # H5个人中心，修改密码
    def change_password(self):
        self.d = u2.connect_usb(self.get_deviceid())
        self.d.app_start(self.ap)
        self.d(text="修改密码").click()
        self.d.xpath('//*[@resource-iself.d="layout"]/anself.droiself.d.view.View[4]').click()
        self.d.senself.d_keys("bn123456", clear=True)
        self.d.xpath('//*[@resource-iself.d="layout"]/anself.droiself.d.view.View[5]').click()
        self.d.senself.d_keys("bn123456", clear=True)
        self.d(text="确认").click()
        pass
    # H5个人中心绑定手机
    def bind_phone(self):
        pass
    # H5个人中心解绑手机
    def unbind_phone(self):
        pass
    # 客服界面
    def customer_service(self):
        pass
    # 论坛
    def forum(self):
        pass
    #判断控件是否存在
    def is_element_appearance(self, locator):
        """目的：检查元素是否出现
        查找步骤：1、先用id找， 2、然后再用xpath
        """
        self.d = u2.connect_usb(self.get_deviceid())
        if self.d(resourceId=locator):
            return True
        else:
            pass




