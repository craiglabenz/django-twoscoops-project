# System
import json

# Django
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# 3rd Party
from annoying.decorators import render_to

def logout_view(request):
    nextUrl = request.GET.get('next',  settings.LOGIN_REDIRECT_URL)
    logout(request)
    return redirect(nextUrl)

@login_required
@render_to('profile.html')
def user_profile(request):
    return {}
