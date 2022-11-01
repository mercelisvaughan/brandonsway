from contextlib import nullcontext
from tkinter import N
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from brandon.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_SUPER_HOST


# Create your views here.
def index(request):
    if request.method == "POST":

        name = request.POST['name']
        subject = request.POST['subject']
        fromEmail = request.POST['email']
        messageText = request.POST['messageText']

        formattedSubject = "Email sent from: " + fromEmail + '<br>' + "Name: " + name + '<br>' + "Message: " + messageText
        
        message = MIMEMultipart('alternative', None, [MIMEText(formattedSubject, 'html')])

        message['Subject'] = subject

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, EMAIL_SUPER_HOST, message.as_string())
            server.quit()
            print("email sent")

        except Exception as e:
            print(f'Error in sending email: {e}')

        #render(request, 'index.html', {'name': name, 'email': email, 'subject': subject, 'message': message})
    return render(request, 'index.html', {})