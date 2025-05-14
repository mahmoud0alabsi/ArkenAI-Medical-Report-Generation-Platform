from django.http import HttpResponse
from django.shortcuts import redirect

from django.utils import timezone

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def admin_only(view_fun):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group != 'admin':
           return redirect('APP_1:dashboard')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
