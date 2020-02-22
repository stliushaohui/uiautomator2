#!/usr/bin/env python
# 此文件，是把Appium API的常用方法封装成一个类
# 这样可以很方便地进行调用。
# 把 Appium 的操作封装成各种函数
import os
import sys
import traceback
import random
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class AndroidDriver(object):
    def __init__(self):

        with open('.\\bn_test\\file\\package.txt')  as f :
            self.ap = f.read()
        # with open('F:\\bn_sszg_test\\file\\activity.txt') as f :
        #     ac = f.read()
        self.bnsdk_app_desired_caps = {
            'platformName': 'Android',
            'deviceName': '48e7de61',
            # 'deviceName': 'P7CDU18402000714',
            'port': '4723',
            'bootstrap - port': '4726',
            'appPackage': self.ap,
            # 'appActivity': ac,
            'appActivity':'prj.iyinghun.platform.sdk.SplashScreenActivity',
            #不清数据
            'noReset': "True",
            'dontStopAppOnReset':'True',
            # 'unicodeKeyboard': True,
            'resetKeyboard': True,
            # 'newCommandTimeout': 600
        }
        # self.bnsdk_app_desired_caps1 = {
        #     'platformName': 'Android',
        #     'deviceName': '48e7de61',
        #     'port': '4724',
        #     'bootstrap - port': '4725',
        #     'appPackage': self.ap,
        #     # 'appActivity': ac,
        #     'appActivity':'com.game.sdk.GameSdkActivity'
        #     # 'unicodeKeyboard': True,
        #     # 'resetKeyboard': True,
        #     # 'newCommandTimeout': 600
        # }
        self.appium_url = 'http://127.0.0.1:4723/wd/hub'  # hub 服务器
    def first(self):
        """初始化各种参数，并连接Appium Server等等"""
        self.driver = webdriver.Remote(self.appium_url,self.bnsdk_app_desired_caps)
        # self.driver.implicitly_wait(15)
    @staticmethod
    def print_exception_message():
        """定义一个静态方法，用于输出标准的错误信息"""
        print("Exception in AndroidDriver:")
        print('-' * 30 + '错误信息请看下方' + '-' * 30)
        print(traceback.print_exc(file=sys.stdout))

    def capture_screenshots(self, file_path=None):
        if file_path is None:
            # if not os.path.exists("./screen_shots"):
            if not os.path.exists("./sdk_screen_shots"):
                # 判断截图目录是否存在，不存在则创建
                os.makedirs("./sdk_screen_shots")
            gamename = self.ap.split('.')[-1]
            path = './sdk_screen_shots/'+gamename+'_%s.png' % time.strftime("%Y-%m-%d %H-%M-%S")
            # path = './sdk_screen_shots/sszg_%s.png' % time.strftime("%Y-%m-%d %H-%M-%S")
            self.driver.get_screenshot_as_file(filename=path)
            if os.path.exists(path):
                return path
            else:
                return False
        else:
            self.driver.get_screenshot_as_file(file_path)
            if os.path.exists(file_path):
                return file_path
            else:
                return False

    def is_element_appearance(self, locator):
        """目的：检查元素是否出现
        查找步骤：1、先用id找， 2、然后再用xpath
        """
        try:
            self.driver.find_element_by_id(locator)
            return True
        except NoSuchElementException:
            pass
        # try:
        #     self.driver.find_element_by_xpath(locator)
        #     return True
        # except NoSuchElementException:
        #     pass
        # try:
        #     self.driver.find_element_by_accessibility_id(locator)
        #     return True
        # except NoSuchElementException:
        #     pass
        return False

    def type_by_id(self, locator, text):
        """根据id找到要输入的位置，并向其发送文本"""
        try:
            self.driver.find_element_by_id(locator).clear()
            self.driver.find_element_by_id(locator).send_keys(text)
            return True
        except Exception as e:
            AndroidDriver.print_exception_message()
            return False

    def type_by_xpath(self, locator, text):
        """根据xpath找到要输入的位置，并向其发送文本"""
        try:
            self.driver.find_element_by_xpath(locator).send_keys(text)
            return True
        except Exception as e:
            AndroidDriver.print_exception_message()
            return False

    def click_by_id(self, locator):
        """根据id来点击
        1、先使用 find_element_by_id
        2、再使用 find_element_by_accessibility_id"""
        try:
            self.driver.find_element_by_id(locator).click()
            return True
        except Exception:
            pass
        try:
            self.driver.find_element_by_accessibility_id(locator).click()
            return True
        except Exception as e:
            pass
        return False

    def click_by_xpath(self, locator):
        """点击xpath"""
        try:
            self.driver.find_element_by_xpath(locator).click()
            return True
        except Exception as e:
            AndroidDriver.print_exception_message()
            return False

    def swipe_to_down(self, duration=200):
        """向下滑动的操作"""
        # 注释
        driver = self.driver
        starty = driver.get_window_size()['height'] * 4/5
        # print(starty)
        endy = driver.get_window_size()['height'] * 1/5
        x = driver.get_window_size()['width'] * 1/2

        try:
            self.driver.swipe(x, starty, x, endy, duration)
            return True
        except Exception:
            # 如何出现异常，就转到这里
            AndroidDriver.print_exception_message()
            return False
    #快速游戏方法
    def quick_register(self):
        #点击快速游戏按钮
        try:
            # self.driver.implicitly_wait(20)
            time.sleep(3)
            self.click_by_id('快速游戏')
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #手机登录方法
    def phone_login(self):
        try:
            # 点击手机登录按钮
            self.driver.implicitly_wait(20)
            self.click_by_id('手机登录')
            self.capture_screenshots()
            # 输入手机号码
            phone = '18024179019'
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_phone',phone)
            self.capture_screenshots()
            # 点击下一步
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_btn_next')
            self.capture_screenshots()
            # 输入验证码
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]').send_keys('000000')
            # 点击登录
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_btn_login')
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #账号登录
    def account_login(self):
        try:
            self.driver.implicitly_wait(20)
            self.click_by_id('账号登录')
            time.sleep(2)
            username = 'lshbnbn'
            password = '123456'
            # 输入账号
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_username', username)
            # 输入密码
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_password', password)
            time.sleep(2)
            # 点击登录按钮
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/yh_btn_sure')
            self.capture_screenshots()
            return True
        except Exception:
            return False
    #账号注册
    def account_register(self):
        try:
            self.driver.implicitly_wait(20)
            self.click_by_id('账号登录')
            self.capture_screenshots()
            # 点击账号注册按钮
            self.click_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]')
            self.capture_screenshots()
            # 输入账号
            username = 'bnuser' + str(random.randint(1000, 10000000))
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_username', username)
            self.capture_screenshots()
            # 输入密码
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_password', 'bn123456')
            # 点击注册按钮
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/yh_btn_sure')
            self.capture_screenshots()
            return True
        except Exception:
            return False
    #用户协议、隐私协议，忘记密码
    def forget_password(self):
        try:
            self.driver.implicitly_wait(20)
            self.click_by_id('账号登录')
            self.capture_screenshots()
            # # 点击用户隐私协议按钮
            # self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_tv_agreement')
            # self.capture_screenshots()
            # # 用户隐私协议页面点击关闭按钮
            # self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/yh_iv_close')
            # self.capture_screenshots()
            #点击账号注册按钮
            self.click_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]')
            # 点击忘记密码按钮
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_tv_forget')
            # 输入手机号
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_phone','18024179019')
            # 点击获取验证码按钮
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_btn_verify')
            # 输入验证码
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_verify', '000000')
            self.capture_screenshots()
            # 输入密码
            self.type_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_edt_password', 'bn123456')
            # 点击修改密码按钮
            self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_btn_login')
            self.capture_screenshots()
            return True
        except Exception:
            return False
    # #token登录
    def token_login(self):
        # self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.switch_to.context(self.driver.contexts[0])
        self.capture_screenshots()
        # while True:
        #     if self.is_element_appearance(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_btn_login')==True:
        self.click_by_id(self.bnsdk_app_desired_caps['appPackage'] + ':id/bn_btn_login')
            #     break
            # else:
            #     break
    # #使用其他账号登录
    def other_login(self):
        try:
            # self.driver.implicitly_wait(20)
            time.sleep(5)
            self.driver.switch_to.context(self.driver.contexts[0])
            time.sleep(5)
            self.click_by_id(self.bnsdk_app_desired_caps["appPackage" ] + ':id/bn_tv_other')
            return True
        except Exception:
            return False
    #下次再说按钮，绑定手机
    def next_time(self):
        self.capture_screenshots()
        while True:
            time.sleep(2)
            if self.is_element_appearance(self.bnsdk_app_desired_caps['appPackage'] + ':id/yh_btn_left') == True:
                self.click_by_id(self.bnsdk_app_desired_caps['appPackage']+':id/yh_btn_left')
                break
            else:
                break
    #悬浮窗按钮，点击悬浮窗，点击退出登录操作
    def xfc(self):
        time.sleep(10)
        y = 1030
        try:
            while True:
                if y in range(1030, 1980):
                # if y in range(1230, 1780):
                    y += 80
                    TouchAction(self.driver).tap(x=14, y=y).perform()
                    print('点击悬浮窗')
                else:
                    break
            time.sleep(2)
            self.capture_screenshots()
            return True
        except Exception:
            return False
    #点击个人中心退出登录按钮
    def lagout(self):
        try:
            # self.driver.implicitly_wait(20)
            time.sleep(3)
            self.capture_screenshots()
            self.click_by_xpath('//*[@id="user-center"]/div/a')
            # self.click_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]')
            return True
        except Exception:
            return False
    #获取权限按钮
    def get_permission(self):
        self.driver.implicitly_wait(20)
        while True:
            # if self.is_element_appearance('android:id/button1') == True:
            if self.is_element_appearance('com.android.packageinstaller:id/permission_allow_button') == True:
                # self.driver.find_element_by_id('android:id/button1').click()
                self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
                self.capture_screenshots()
            time.sleep(2)
            if self.is_element_appearance('com.android.packageinstaller:id/permission_allow_button') == False:
                break
    #H5个人中心，实名认证功能
    def real_name(self):
        try:
            # self.driver.implicitly_wait(20)
            self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            #实名认证
            self.click_by_xpath('//*[@id="user-center"]/a[3]/div[1]/span[2]')#点击实名认证按钮，跳转到实名认证页面
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[1]/input','张三')#输入姓名
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/input','440514199708087833')#输入身份证
            time.sleep(2)
            self.capture_screenshots()
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')#点击实名认证按钮
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #H5个人中心，修改密码
    def change_password(self):
        try:
            # self.driver.implicitly_wait(20)
            # self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            self.click_by_xpath('//*[@id="user-center"]/a[1]/div[1]/span[2]')
            time.sleep(2)
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/input','bn123456')
            time.sleep(2)
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[3]/input','bn123456')
            time.sleep(2)
            # self.capture_screenshots()
            time.sleep(3)
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #H5个人中心绑定手机
    def bind_phone(self):
        try:
            # self.driver.implicitly_wait(20)
            # time.sleep(5)
            # self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            # self.driver.refresh()
            self.click_by_xpath('//*[@id="user-center"]/a[2]/div[1]/span[2]')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[1]/input','18024179019')
            self.click_by_xpath('//*[@id="layout"]/div[1]/div[2]/button')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/div/input','000000')
            time.sleep(2)
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            time.sleep(2)
            self.capture_screenshots()
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #H5个人中心解绑手机
    def unbind_phone(self):
        try:
            # self.driver.implicitly_wait(20)
            # self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            # 点击账户按钮
            self.click_by_xpath('//*[@id="nav-bar"]/a[1]')
            time.sleep(2)
            self.click_by_xpath('//*[@id="user-center"]/a[2]/div[1]/span[2]')
            self.click_by_xpath('//*[@id="layout"]/div[1]/div[2]/button')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/div/input', '000000')
            time.sleep(2)
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            # print(self.driver.current_context)
            time.sleep(2)
            self.capture_screenshots()

            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #客服界面
    def customer_service(self):
        try:
            self.driver.implicitly_wait(20)
            self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(10)
            # 点击个人中心客服按钮
            self.click_by_xpath('//*[@id="nav-bar"]/a[3]')
            # 点击QQ交谈
            self.click_by_xpath('//*[@id="server"]/div[1]/a')
            time.sleep(2)
            # 点击物理返回键
            self.driver.press_keycode(4)
            time.sleep(2)
            # 点击拨打电话
            self.click_by_xpath('//*[@id="server"]/div[2]/a')
            time.sleep(2)
            # 点击物理返回键
            self.driver.press_keycode(4)
            self.driver.press_keycode(4)
            time.sleep(2)
            # 点击拷贝账号
            self.click_by_xpath('//*[@id="copy-wechat"]')
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #论坛
    def forum(self):
        try:
            self.driver.implicitly_wait(20)
            self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            self.click_by_xpath('//*[@id="nav-bar"]/a[2]')#点击个人中心论坛按钮
            time.sleep(3)
            # self.capture_screenshots()
            time.sleep(2)
            # self.driver.close_app()
            # time.sleep(3)
            # self.first()
            self.driver.press_keycode(4)

            return True
        except Exception:
            return False
    #客服、解绑、绑定
    def ke_bi_fo(self):
        try:
            self.driver.implicitly_wait(20)
            self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            # 点击个人中心客服按钮
            self.click_by_xpath('//*[@id="nav-bar"]/a[3]')
            # 点击QQ交谈
            self.click_by_xpath('//*[@id="server"]/div[1]/a')
            time.sleep(2)
            # 点击物理返回键
            self.driver.press_keycode(4)
            time.sleep(2)
            # 点击拨打电话
            self.click_by_xpath('//*[@id="server"]/div[2]/a')
            time.sleep(2)
            # 点击物理返回键
            self.driver.press_keycode(4)
            self.driver.press_keycode(4)
            time.sleep(2)
            # 点击拷贝账号
            self.click_by_xpath('//*[@id="copy-wechat"]')
            time.sleep(2)
            self.click_by_xpath('//*[@id="nav-bar"]/a[1]')
            #点击账户按钮
            self.click_by_xpath('//*[@id="nav-bar"]/a[3]')
            #解绑、绑定
            time.sleep(2)
            self.click_by_xpath('//*[@id="user-center"]/a[2]/div[1]/span[2]')
            self.click_by_xpath('//*[@id="layout"]/div[1]/div[2]/button')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/div/input', '000000')
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            time.sleep(2)
            self.capture_screenshots()
            time.sleep(2)
            self.click_by_xpath('//*[@id="user-center"]/a[2]/div[1]/span[2]')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[1]/input', '18024179019')
            self.click_by_xpath('//*[@id="layout"]/div[1]/div[2]/button')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/div/input', '000000')
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            time.sleep(2)
            self.capture_screenshots()
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
    #实名认证、改密码
    def re_cha(self):
        try:
            self.driver.implicitly_wait(20)
            time.sleep(5)
            self.driver.switch_to.context(self.driver.contexts[1])
            time.sleep(2)
            #实名认证
            self.click_by_xpath('//*[@id="user-center"]/a[2]/div[1]/span[2]')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[1]/input','18024179019')
            self.click_by_xpath('//*[@id="layout"]/div[1]/div[2]/button')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/div/input','000000')
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            time.sleep(2)
            self.capture_screenshots()
            #改密码
            time.sleep(2)
            self.click_by_xpath('//*[@id="user-center"]/a[1]/div[1]/span[2]')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[2]/input', 'bn123456')
            self.type_by_xpath('//*[@id="layout"]/div[1]/div[3]/input', 'bn123456')
            time.sleep(2)
            self.capture_screenshots()
            self.click_by_xpath('//*[@id="layout"]/div[1]/a')
            return True
        except Exception:
            AndroidDriver.print_exception_message()
            return False
