#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SunWei
# @Time    : 
# @language: python2.7
from fabric.colors import *
from fabric.api import *

env.user='root'
env.roledefs={                 #主机分组

    'websevers':[],
    'dbservers':[]
}
env.passwords = {

}


@roles('webservers')
def webtask():                     #部署nginx环境
    print yellow("install nginx php php-fpm...")
    with settings(warn_only=True):
        run('apt-get -y install nginx')
        run('apt-get -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd')
        run('chkconfig --levels 235 php-fpm on')
        run('chkconfig --levels 235 nginx on')

@roles('dbserver')
def dbstask():                     #部署mysql环境
    print yellow("Install Mysql...")
    with settings(warn_only=True):
        run('apt-get -y install mysql mysql-server')
        run('chkconfig --levels 235 mysql on')

@roles('webservers', 'dbservers')
def publictask():                   #部署公共类环境
    print yellow('Install epel ntp...')
    with settings(warn_only=True):
        run("rpm -Uvh http://dl.fedorapioject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run('apt-get -y install ntp')

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbstask)