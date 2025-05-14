from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from app.ai_code import get_response
from django.contrib.auth.decorators import login_required
from app.models.records.models import *
from app.models.users.models import *
from app.forms.profile_forms import *

@login_required(login_url='app:login')
def ProfilePage(request):
    context={'active_side_nav_item':'profile', "page_title": "Profile", 'sub_dir':True, 'sub_dir_name':'Profile'}
    
    user = request.user
    profile = ProfileInfo.objects.get(user=user)
    
    form = EditProfileInfoForm(instance=profile)

    if request.method == 'POST':
        if 'update_info_btn' in request.POST:
            form = EditProfileInfoForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('app:profile')

        
        elif 'delete_user_btn' in request.POST:
            user.delete()
            return redirect('app:login')

    context['update_form'] = form
    context['profile'] = profile

    return render(request, 'dash_temp/profile.html', context)