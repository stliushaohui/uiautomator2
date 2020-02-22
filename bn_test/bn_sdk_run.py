import tkinter
from bn_test.lib.TestResult import Report
from bn_test.testcase.gjsg_test import GjsgTest
import sys


#挂机三国
def test_gjsg():
    r = Report()
    # 执行测试用例
    suite = r.get_suite(case=GjsgTest)
    # 生成测试报告
    r.report_html(suite)
# #暴走神话
# def test_bzsh():
#     r = Report()
#     #执行测试用例
#     suite = r.get_suite(case=BzshCase)
#     #生成测试报告
#     r.report_html(suite)