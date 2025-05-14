from django.shortcuts import render, redirect
from app.decorators import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.urls.base import reverse

from app.models.book.book_form import BookDemoForm

@unauthenticated_user
def HomePage(request):
    context={}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        institution = request.POST.get('institution')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        form = BookDemoForm(data={'name':name, 'email':email, 'institution':institution, 'phone':phone, 'subject':subject, 'message':message},)

        if form.is_valid():
            form.save()

            message = '''
            From:\n\t\t{}\n
            Subject:\n\t\t{}\n
            Message:\n\t\t{}\n
            Email:\n\t\t{}\n
            Institution:\n\t\t{}\n
            Phone:\n\t\t{}\n
            '''.format(name, subject, message, email, institution, phone)
            send_mail(
                subject=subject,
                message=message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER])
                    # TODO: enter your email addre
            
            
            return JsonResponse(
                {
                    "url": reverse("app:home"),
                    "success": True,
                }
            )

        else:
            
            return JsonResponse(
                {
                    "url": reverse("app:home"),
                    "success": False,
                }
            )


    return render(request, 'home_temp/index.html', context)