# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate
from django.contrib.auth import login
import logging
logger = logging.getLogger("holyshit")


@require_POST
def login_action(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user:
        login(request, user)
        return redirect("account:account_profile_view")
    else:
        return redirect("account:account_login_view")


@require_POST
def regist_action(request):
