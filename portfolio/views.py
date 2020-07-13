from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import Portfolio

# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'index.html', {'portfolios': portfolios})

def porties(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolios.html', {'portfolios': portfolios})

def mail(request):
    if request.method == 'POST':
        subject = 'YOUR PORTFOLIO SITE'
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message'] + ' from ' +name + ' : ' + email + ' : ' + phone
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mnnlthmpsn@outlook.com','artbychel29@gmail.com']

        send_mail( subject, message, email_from, recipient_list )
        messages.add_message(request, messages.SUCCESS, 'Mail Sent')
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))