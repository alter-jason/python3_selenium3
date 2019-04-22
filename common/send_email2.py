import os,smtplib,os.path
from email.mime.application import MIMEApplication

import time

from config import proterty as gl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import log
'''
邮件发送最新的测试报告
'''


class send_email2:
		def __init__(self):
			self.mylog = log.log()

		def send_initmail(self,file_new):

		# 发件人邮箱
			mail_from = 'zj.xxq@163.com'
		# 收件人邮箱
			mail_to = ['591785945@qq.com','zj.xxq@163.com']
		# 定义正文
			f = open(file_new, 'rb')
			mail_body = f.read()
			f.close()
			msg = MIMEMultipart()#定义邮件为多个部分
			#正文部分
			msg_body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
			msg.attach(msg_body)
			#附件部分
			html_part = MIMEApplication(mail_body)
			html_part.add_header('Content-Disposition', 'attachment', filename='test_report.html')
			msg.attach(html_part)

			# 定义标题
			msg['Subject'] = u"'Python email "
			# 发件人
			msg['From'] = mail_from
			# 收件人，必须是一个字符串
			msg['To'] = ','.join(mail_to)
			# 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
			msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
			smtp = smtplib.SMTP_SSL('smtp.163.com',465)
			# 连接 SMTP 服务器，此处用的 163 的 SMTP 服务器
			smtp.connect('smtp.163.com')
			# 发件人的用户名密码
			smtp.login('zj.xxq', 'zj145678')
			try:
				#发送邮件
				smtp.sendmail(mail_from, mail_to, msg.as_string())
				smtp.quit()
				print ('email has send out !')
			except smtplib.SMTPException:
				self.mylog.error(u'邮件发送测试报告失败 at' + __file__)


		# ======查找测试报告目录，找到最新生成的测试报告文件====
		def send_report(self):
			report_list = os.listdir(gl.report_path)
			report_list.sort(
				key=lambda fn: os.path.getmtime(gl.report_path + fn) if not os.path.isdir(gl.report_path + fn) else 0)
			new_report = os.path.join(gl.report_path, report_list[-1])
			print(new_report)
			# 发送邮件
			self.send_initmail(new_report)