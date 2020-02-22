import HTMLReport
import time
import unittest
import os
import yagmail


class Report(object):
    def __init__(self):
        print('开始执行测试：')

    # 执行测试用例
    def get_suite(self, case):
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTests(loader.loadTestsFromTestCase(case))
        return suite
    #生成测试报告
    def report_html(self,suites):
        HTMLReport.TestRunner(report_file_name='results_%s.html'%time.strftime("%Y-%m-%d %H-%M-%S"),title='sdk自动化测试',description='SDK测试结果如下：').run(suites)
        print('生成报告完毕!')
    #读取要发送的最新报告路径
    def new_report(self,test_dir):
        lists =  os.listdir(test_dir)
        lists.sort(key=lambda fn:os.path.getctime(test_dir+'\\'+fn))
        file_path = os.path.join(test_dir,lists[-1])
        return file_path
    #发送测试报告
    def send_report(self,test_dir,username,password,rece):
        yag = yagmail.SMTP(host='smtp.163.com',user=username,password=password)
        att = self.new_report(test_dir)
        yag.send(to=rece,subject='冰鸟自动化测试报告',contents='附件为自动化测试报告',attachments=att)
        print('发送成功')
