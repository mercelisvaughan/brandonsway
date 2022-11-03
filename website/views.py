from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


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
            server.login('brandonswayprp51@gmail.com', 'pfwrpkfwjfqyksdk')
            server.sendmail('brandonswayprp51@gmail.com', 'mercelisvaughan@gmail.com', message.as_string())
            server.quit()
            print("email sent")
            logging.info('email has been sent')
            

        except Exception as e:
            logging.info('Error in email')
            print(f'Error in sending email: {e}')

        
        logging.info('Index has been loaded')
    return render(request, 'index.html', {})