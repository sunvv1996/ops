#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SunWei
# @Time    :
# @language: python2.7

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


HOST = "smtp.isoftstone.com"    #定义host主机
SUBJECT = u"spit0124周报"       #定义邮件主题
TO = "@163.com"      #定义邮件收件人
FROM = "@isoftstone.com" #定义邮件发送人

def addimg(src,imgid):
    fp = open(src,'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)

    return msgImage

msg = MIMEMultipart('related')    #创建MIMEMultipart对象，采用related定义内嵌资源的邮件体

msgtext = MIMEText("<font color=red>0124周报:\n<br><img src=\"cid:weekly\" border=\"1\"/></br>详情见附件</font>","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/111.jpg","weekly"))


attach = MIMEText(open("doc/week_report.xlsx", "rb", ).read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"  #指定文件格式类型
attach["Content-Disposition"] = "attachment; filename=\" spit0124周报.xlsx\"".decode("utf-8").encode("gb18030")
#指定Content-Disposition值为attachment则出现下载保存框

msg.attach(attach)   #MIMEMultipart对象附加MIMEText附件内容
msg['Subject'] = SUBJECT    #邮件主题
msg['From'] = FROM       #邮件发件人，头部可见
msg['TO'] = TO       #邮件收件人，头部可见
try:
    server = smtplib.SMTP()
    server.connect(HOST, "25")
    server.starttls()
    server.login("weisunq@isoftstone.com","power@2020")  #邮箱帐号登录校准
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print u"邮件发送成功  [ok]"
except Exception,e:
    print u"失败  [error]"+str(e)

input()
