# -*- coding: utf-8 -*-
import os
import smtplib
import unittest
import time
from email.header import Header
from email.mime.text import MIMEText
from conf.settings import report_path, send_email_path, receive_email_path, email_authorization_code, message_title


# 定义发送邮件
def send_mail(file_new):
    f = open(file_new, "rb")
    mail_body = f.read()
    f.close()
    # 编写HTML类型邮件正文
    msg = MIMEText(mail_body, "html", "utf-8")
    msg["Subject"] = Header(message_title, "utf-8")

    # 发送邮箱服务器
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    # 发送邮箱用户/qq邮箱smtp的授权码
    smtp.login(send_email_path,email_authorization_code)
    # 发送邮箱/接收邮箱/邮件主题
    smtp.sendmail(send_email_path,receive_email_path,msg.as_string())
    smtp.quit()
    print("邮件已发送")

# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(test_report):
    lists = os.listdir(test_report)
    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

if __name__=="__main__":
    # 发送测试报告到邮箱
    new_report = new_report(report_path)
    send_mail(new_report)