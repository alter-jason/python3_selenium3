# coding:utf-8
from common import send_email2
import unittest,time
from config.proterty import test_case_path,report_name
from config import HTMLTestRunner
'''
构建测试套件，并执行测试
'''


# 构建测试集
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test_baidu.py')

# 执行测试
if __name__=="__main__":
    report = report_name+"Report.html"
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestReportCN(
        stream=fb,
        title=u'自动化测试报告',
        description=u'项目描述。百度测试',
        tester = u'周军'
    )
    runner.run(suite)
    fb.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕
    # email = send_email2.send_email2()
    # email.send_report()