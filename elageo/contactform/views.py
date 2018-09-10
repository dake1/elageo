from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def contactus(request):
    current_page='contactus'
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "{} from {} ({})".format(cd['subject'], cd['name'],cd['email'])
            sender= cd['name'],
            email = cd['email']
            message = cd['message']
            send_mail(subject, message, email,['geomappersconsult@yahoo.com',])
            # messages.success(request,'Message sent successfully')
            return redirect('mailsent')

    else:
        form = ContactForm()

    return render(request,'contactform/contactus.html',{'form':form,
                                                        'current_page':current_page})


def mailsent(request):
    return render(request,'contactform/mailsent.html',{})
