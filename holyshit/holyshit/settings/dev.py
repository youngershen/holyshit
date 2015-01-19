# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from base import *

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = env('HOLYSHIT_SECRET_KEY', default='are you thinking what i am thinking')

SALT = env('HOLYSHIT_SALT', default='younger is everything')

DATABASES = {
    "default": env.db_url('HOLYSHIT_DB_DEV', default='mysql://root:root@127.0.0.1:3306/holyshit_dev')
}

INSTALLED_APPS += ('debug_toolbar',)

