#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","CrazyEye.settings")
    import django
    django.setup()
    from backend import main

    obj = main.HostManager()
    obj.interactive()