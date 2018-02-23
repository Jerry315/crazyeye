#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os,time,json
from concurrent.futures import ThreadPoolExecutor
import paramiko

def ssh_cmd(task_log_obj):
    host = task_log_obj.bind_host.host
