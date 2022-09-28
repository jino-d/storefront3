from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Jino'}
        )
        message.send(['jcdologmanding@spectrumone.co'])
        # message = EmailMessage(
        #      'subject',
        #     'message',
        #     'jino.c.dologmanding@gmail.com',
        #     ['jcdologmanding@spectrumone.co'],
        # )
        # message.attach_file('playground/static/images/bg.jpeg')
        # message.send()
        # mail_admins(
        #     'subject',
        #     'message',
        #     html_message='message'
        # )
        # send_mail(
        #     'subject',
        #     'message',
        #     'jino.c.dologmanding@gmail.com',
        #     ['jcdologmanding@spectrumone.co'],
        # )
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Jino'})
