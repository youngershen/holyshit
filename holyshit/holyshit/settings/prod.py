# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from base import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = env('HOLYSHIT_SECRET_KEY')

SALT = env('HOLYSHIT_SALT')

DATABASES = {
    "default": env.db_url('HOLYSHIT_DB_PROD')
}
