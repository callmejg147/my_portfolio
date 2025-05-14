from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .email import E_HOST_USER


def home_view(request):
    
    return render(request, 'index.html', context = {})

def s_mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        message = request.POST.get('msg')
        
        send_mail(
            subject= 'Portfolio',
            message= f'{name}\n{phone}\n{mail}\n\n{message}',
            from_email = E_HOST_USER,
            recipient_list= ['jithin.george14796@gmail.com'],
            fail_silently= False
        )
        return redirect('/')
        