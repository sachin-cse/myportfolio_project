from django.shortcuts import render
from django.http import HttpResponse
from .models import About
from .models import Skills
from .models import Contact
from django.contrib import messages


def home(request):
    link2={
        'twitter':'https://twitter.com/SachinM71986260?t=VxgzosvpvARwzeFjnQJgjg&s=08',
        'facebook':'https://www.facebook.com/sachin.mandal.7773631',
        'instagram':'https://www.instagram.com/mandal_sachin12/',
        'github':'https://github.com/sachin-cse',
        'linkdln':'https://www.linkedin.com/in/sachin-mandal-2a894820a',
    }
    return render(request,'index.html',link2)

def about(request):
    data1 = About.objects.all()
    links = {
        'twitter':'https://twitter.com/SachinM71986260?t=VxgzosvpvARwzeFjnQJgjg&s=08',
        'facebook':'https://www.facebook.com/sachin.mandal.7773631',
        'instagram':'https://www.instagram.com/mandal_sachin12/',
        'github':'https://github.com/sachin-cse',
        'linkdln':'https://www.linkedin.com/in/sachin-mandal-2a894820a',
        'data1':data1
    }
    return render(request,'About.html',links)

def contact(request):
    link1={
        'twitter':'https://twitter.com/SachinM71986260?t=VxgzosvpvARwzeFjnQJgjg&s=08',
        'facebook':'https://www.facebook.com/sachin.mandal.7773631',
        'instagram':'https://www.instagram.com/mandal_sachin12/',
        'github':'https://github.com/sachin-cse',
        'linkdln':'https://www.linkedin.com/in/sachin-mandal-2a894820a',
    }
    return render(request,'contact.html',link1)

def resume(request):
    skill=Skills.objects.all()
    links = {
        'twitter':'https://twitter.com/SachinM71986260?t=VxgzosvpvARwzeFjnQJgjg&s=08',
        'facebook':'https://www.facebook.com/sachin.mandal.7773631',
        'instagram':'https://www.instagram.com/mandal_sachin12/',
        'github':'https://github.com/sachin-cse',
        'linkdln':'https://www.linkedin.com/in/sachin-mandal-2a894820a',
        'skill':skill
    }
    return render(request,'resume.html',links)

def message(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        education=request.POST.get('education')
        message=request.POST.get('message')
        ins=Contact(name=name, email=email, address=address, education=education, message=message)
        ins.save()
        messages.success(request,'Your Contact submitted successfully. We will reply soon.')
    return render(request,'submit.html')



    



