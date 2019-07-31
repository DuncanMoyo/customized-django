from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Email ourselves the submitted contact message

        subject = 'Contact Form Received'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.DEFAULT_FROM_EMAIL]

        # OPTION 1
        #contact_message = '{0}, from {1} with email {2}'.format(message, name, email)

        # OPTION 2
        context = {
            'user': name,
            'email': email,
            'message': message
        }

        contact_message = get_template('contact_message.txt').render(context)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

        return redirect('/other/')
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'other.html', {})
