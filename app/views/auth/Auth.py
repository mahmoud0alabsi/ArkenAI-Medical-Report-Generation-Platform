from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from app.ai_code import get_response
from django.contrib.auth import authenticate, login, logout
from app.models.users.models import *
from app.decorators import *

@unauthenticated_user
def LoginPage(request):
    context={'active_side_nav_item':'login', "page_title": "Login", 'sub_dir':False, 'sub_dir_name':'Login'}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)
            return JsonResponse(
                {
                    "url": reverse("app:dashboard"),
                    "success": True,
                }
            )
        else:
            return JsonResponse(
                {
                    "url": reverse("app:login"),
                    "success": False,
                }
            )
            

    return render(request, 'auth_temp/sign-in.html', context)



def LogoutPage(request):
    logout(request)
    return redirect('app:login')