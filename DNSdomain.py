# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#dns域名轮询监控

import dns.resolver
import os
import http.client

iplist = []
appdomain = 'hao123.com'

def get_iplist(domain = ""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print('dns resover error:'+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip +":80"
    getcontent = ""
    conn = http.client.HTTPConnection(checkurl, timeout=5)

    try:
        conn.request("GET", "/", headers={"HOST":appdomain})

        r = conn.getresponse()
        getcontent = r.read(15)

    finally:
        if getcontent=="<!Doctype html>":
            print(ip+ "[ OK]")
        else:
            print(ip+"[ ERROR]")

if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")




