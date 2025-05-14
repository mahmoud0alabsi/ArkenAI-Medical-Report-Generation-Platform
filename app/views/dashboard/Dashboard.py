import os
import time
from pathlib import Path
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from app.ai_code import get_response
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from django.contrib.auth.decorators import login_required
from app.models.records.models import *
from app.models.users.models import *
from app.decorators import *

from app.ai_code import *

# In this view, we save user attemp evenbefore the user saves itself,
# and it saved in TempRecords database. When the user saves itself again
# we save the record in SaveRecords database.
#
# Note that we have to delete the record saved in TempRecords database
# every day  

@login_required(login_url='app:login')
def DashboardPage(request):
    context={'active_side_nav_item':'dashboard', "page_title": "Dashboard", 'sub_dir':False,}

    if request.method == "POST":

        if 'submit_recorded_audio' in request.POST or 'submit_uploaded_audio' in request.POST:

            audio_file = request.FILES.get('recorded_audio')
            
            # to avoide similarity in recorded files names, we put id in name
            if 'submit_recorded_audio' in request.POST:
                recorded_file = True
                tmp = TempRecord.objects.last().id
                audio_file.name = f'audiorecord_{tmp}.webm'
            else:
                recorded_file = False
            
            record = TempRecord.objects.create(user=request.user, voice_record=audio_file, recorded=recorded_file)
            record.save()
            

            # convert record audio format to mp3 format
            if 'submit_recorded_audio' in request.POST:
                new_audio_file_path = str(str(record.voice_record.path).split('.')[0] + '.mp3')
                new_audio_file_name = record.voice_record.name.split('.')[0] + '.mp3'

                ffmpeg_extract_audio(record.voice_record.path, new_audio_file_path)
                os.remove(record.voice_record.path)

                record.voice_record = new_audio_file_name
                record.save()


            
            # send audio file path to ai_code file, for transcribt and generate report
            result = get_response(record.voice_record.path)

            record.original_response = result['response']
            record.save()

            user_profile = ProfileInfo.objects.get(user=request.user)
            user_profile.num_of_sub += 1
            user_profile.save()
            
            return JsonResponse(
                {
                    "url": reverse("app:dashboard"),
                    "success": True,
                    'response' : result['response']
                }
            )

        
        elif 'submit_save_response' in request.POST:
            Text = request.POST.get('outputTextarea')  # get report from textarea because user maybe edit report before save it
            Title = request.POST.get('reportTitle')    # get report title

            all_record = TempRecord.objects.filter(user = request.user).order_by('-date_created') # get all user attempts saved in TempRecord Database
            record = all_record[0]  # get last one saved to save it to SaveRecord database

            saved_record = SavedRecord.objects.create(user=request.user, voice_record=record.voice_record,
                           title=Title, original_response=record.original_response, saved_response=Text,
                           recorded=record.recorded)

            saved_record.save()
            
            return JsonResponse(
                {
                    "url": '',
                    "success": True,
                    'response' : ['Saving Done!'],
                }
            )

    return render(request, 'dash_temp/dashboard.html', context)