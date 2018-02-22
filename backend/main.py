# _*_ coding:utf-8 _*_
# Auother Jerry
from web import models
import sys
from django.contrib.auth import authenticate

class HostManager(object):
    '''用户登录堡垒机后的交互程序'''

    def __init__(self):
        self.user = None

    def interactive(self):
        '''交互脚本'''
        print("-----run-----")

        count = 0
        while count < 3:
            username = input("Username:").strip()
            password = input("Password").strip()
            user = authenticate(username=username,password=password)
            if user:
                print("Welcome %s".center(50,'-') % user.name)
                self.user = user
                break
            else:
                print("Wrong user or password")
            count += 1
        else:
            sys.exit("Too many attemps, bye")

        if self.user: #验证成功
            for index,host_group in enumerate(self.user.host_groups.all()):
                print("%s.\t%s[%s]" % (index,host_group.name,host_group.bind_hosts.count()))
            print("z.\t未分组主机[%s]" %(self.user.bind_hosts.count()))