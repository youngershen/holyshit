from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET


@login_required
def index_view(request):
    return redirect(reverse("account:account_profile_view"))


@login_required
def profile_view(request):
    return HttpResponse("haha")


@require_GET
def login_view(request):
    if request.user.is_authenticated():
        return redirect("account:account_profile_view")
    else:
        return render(request, 'account/login.html')


@require_GET
def regist_view(request):
    if request.user.is_authenticated():
        return redirect("account:account_profile_view")
    else:
        return render(request, 'account/regist.html')