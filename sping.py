#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SunWei
# @Time    : 2017.01.06
# @language: python2.7
import subprocess
from threading import Thread
from Queue import Queue
from IPy import IP #需安装模块 pip install IPy

num_ping_threads = 256  #线程数
in_queue = Queue()    #队列
out_queue = Queue()

ips = IP("10.130.129.0/24")#写入ip或网段

def ping_scan(i,iq,oq):
    while True:
        ip = iq.get()
                              #可根据情况自行更改ping语句
        ret = subprocess.call("ping -n 1 %s -w 1" % ip, shell=True,stdout=open('ip.txt','w'),stderr=subprocess.STDOUT)
        if ret !=0:
            oq.put(ip)
            print "[*]%s:did not respond"% ip
        else:
            print "[*]%s:--ok--" % ip
        iq.task_done()
for ip in ips:
    in_queue.put(ip)

for i in range(num_ping_threads):
    work = Thread(target = ping_scan,args = (i, in_queue,out_queue))
    work.setDaemon(True)
    work.start()

print "Main Threeding Waiting"
in_queue.join()
print "Done"
input()
