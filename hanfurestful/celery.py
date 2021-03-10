from __future__ import absolute_import, unicode_literals

import os

import django
from django.conf import settings

from celery import Celery, platforms
# from hanfurestful.settings import ROOT_URLCONF

platforms.C_FORCE_ROOT = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hanfurestful.settings')  # 设置django环境
django.setup()

app = Celery('hanfurestful')
app.config_from_object('django.conf:settings') #  使用CELERY_ 作为前缀，在settings中写配置
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)  # 发现任务文件每个app下的task.py
