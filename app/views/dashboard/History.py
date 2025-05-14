import json
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from app.ai_code import get_response
from django.contrib.auth.decorators import login_required
from app.models.records.models import *
from app.models.users.models import *


@login_required(login_url='app:login')
def HistoryPage(request):
    context={'active_side_nav_item':'history', "page_title": "History", 'sub_dir':True, 'sub_dir_name':'History'}

    user = request.user

    all_history = SavedRecord.objects.filter(user=user).order_by('-date_created')

    context['all_history'] = all_history

    if request.method == 'POST':

        if 'display_report_btn' in request.POST:
            print('***** inside btn **********')
            id = request.POST.get('id')

            obj = SavedRecord.objects.get(id=id)

            return JsonResponse(
                {
                    "url": reverse("app:history"),
                    "success": True,
                    'response' : {'id':obj.id, 'voice_record':obj.voice_record.url, 'title':obj.title, 'original_response':obj.original_response, 'saved_response':obj.saved_response, 'date_created':str(obj.date_created)},
                }
            )

        elif 'save_edit_report_btn' in request.POST:

            id = request.POST.get('id')
            newTitle = request.POST.get('newTitle')
            newReport = request.POST.get('newReport')

            obj = SavedRecord.objects.get(id=id)

            obj.title = newTitle
            obj.saved_response = newReport
            obj.save()

            return JsonResponse(
                {
                    "url": reverse("app:history"),
                    "success": True,
                }
            )


        elif 'delete_report_btn' in request.POST:

            id = request.POST.get('id')

            obj = SavedRecord.objects.get(id=id)
            obj.deleteObjWithFile()

            return JsonResponse(
                {
                    "url": reverse("app:history"),
                    "success": True,
                }
            )

    return render(request, 'dash_temp/tables.html', context)

