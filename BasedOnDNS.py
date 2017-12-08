#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SunWei
# @Time    : 2016.12.22
# @language: python2.7
import dns.resolver
import os
import httplib

iplist = []
appdomain = "163.com" #定义业务域名

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception,e:
        print "dns resolver error:" + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)  #追加到iplist
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)  #定义http链接超时时间
    conn = httplib.HTTPConnection(checkurl) #创建http链接对象

    try:
        conn.request("GET", "/",headers = {"Host": appdomain}) #发起url请求，添加host主机头

        r = conn.getresponse()
        getcontent = r.read(6) #或取url页面钱的n个字符，以便做可用性校验
        #print getcontent
    finally:
        if getcontent == "<html>":#监控url页的内容
            print ip+" [ok]"
        else:
            print ip+" [Error]"  # 后期可升级

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist) > 0:  #条件：域名解析正确且至少返回一个Ip
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."

input()