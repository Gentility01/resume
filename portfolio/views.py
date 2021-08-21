# from portfolio.models import Contact
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact


# Create your views here.
def home(request):
    if request.method == 'POST':
        contact = Contact
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        submit = Contact(
            name = name, email=email, subject=subject, message=message
        )
        submit.save()
        return HttpResponse("<h1> Thanks for your contact</h1>")

      

    return render(request, 'portfolio/index.html')
