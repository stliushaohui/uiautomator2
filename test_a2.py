# -*- coding: utf-8 -*-
import uiautomator2 as u2
from time import sleep
# d = u2.connect_usb('P7CDU18402000714')
from bn_test.lib.bn_a2_lib import Bnautomator2
b = Bnautomator2()
d = u2.connect(b.get_deviceid())
# ##获取设备多台设备号列表
# def get_deviceid():
#     str_init=' '
#     all_info= os.popen('adb devices').readlines()
#     print('adb devices 输出的内容是：',all_info)
#
#     for i in range(len(all_info)):
#         str_init+=all_info[i]
#     devices_name=re.findall('\n(.+?)\t',str_init,re.S)
#
#     # print('所有设备名称：\n',devices_name)
#     return devices_name[0]
d.app_start('com.xsgmjl.bingniaozfyl')
sleep(3)
d(resourceId="com.xsgmjl.bingniaozfyl:id/bn_tv_other").click()
d(description="手机登录").click()
d(resourceId="com.xsgmjl.bingniaozfyl:id/bn_edt_phone").click()
d.send_keys("18024179019", clear=True)
d(resourceId="com.xsgmjl.bingniaozfyl:id/bn_btn_next").click()
d.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
d.app_stop('com.xsgmjl.bingniaozfyl')
# d.send_keys("000000", clear=True)
# d.app_stop('com.xsgmjl.bingniaozfyl')
# d.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
# d.send_keys("0", clear=True)
# d.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
# d.send_keys("0", clear=True)
# d.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[4]').click()
# d.send_keys("0", clear=True)
# d.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[5]').click()
# d.send_keys("0", clear=True)
# d.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_verify_view"]/android.widget.LinearLayout[1]/android.widget.TextView[6]').click()
# d.send_keys("0", clear=True)
# driver.xpath('//*[@text="退出登录"]').click()
# driver.xpath('//*[@text="修改密码"]').click()
# driver.xpath('//*[@resource-id="com.xsgmjl.bingniaozfyl:id/bn_vp_content"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').set_text('lshbnb')
# print(driver.info)

# import sys
# import uiautomator2  as u2
# from time import sleep
# import os
# import subprocess
# import threading
# import time
#
# def MultiDevice( d):  # 功能执行
#
#     d.screen_on()
#     # print(d.info)
#     d.screen_off()
#
# def getphonelist():  # 获取手机设备
#     cmd = r'adb devices'  # % apk_file
#     pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#     pr.wait()  # 不会马上返回输出的命令，需要等待
#     out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
#     devices = []
#     for i in (out)[1:-1]:
#         device = str(i).split("\\")[0].split("'")[-1]
#         devices.append(device)
#     return devices  # 手机设备列表
#
#
#
# def test_xxx(i):
#     d = u2.connect(i)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
#     MultiDevice(d)
#
#
# def start():
#         threads = []
#         for i in range(len(getphonelist())):
#             threads.append(threading.Thread(target=test_xxx(getphonelist()[i]),args=()))
#         for t in threads:
#             time.sleep(0.3)
#             t.start()
#         for t in threads:
#             t.join()
# if __name__ == '__main__':
#     start()
