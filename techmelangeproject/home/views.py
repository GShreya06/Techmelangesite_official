from datetime import datetime
from multiprocessing import context
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from .models import festdesc
from .models import events
from .models import contacts
from .models import sponsers
from .models import main
# Create your views here.


def home(request):
    # for main database
    m=main.objects.all();
    #print(m)
    for i in m:
        m1=i.mname
        m2=i.mdesc
        m3=i.mdate
        m4=i.mbg
    # for only first element use first
    #for all objects use all
    
    # for about database
    a=festdesc.objects.all(); 
    #print(a)
    for i in a: 
        # for taking values from database use loop
        a1=i.fest_name 
        a2=i.fest_desc
    
    # for events database
    b=events.objects.all();
    #print(b)
    for i in b:
         e1=i.e_name
    
    c=contacts.objects.all();
    #print(c)
    for i in c:
        c1=i.C_email
        c2=i.C_mobile
    return render(request, 'index.html', {'m1' : m1 ,'m2' : m2 ,'m3' : m3 ,'a1':a1 , 'a2':a2,'b':b ,'e1':e1 , 'c1':c1 , 'c2':c2})

def event(request,event_id):
    b=events.objects.get(id=event_id);
    print(b)
    return render(request, 'event.html', {'b':b})

def sponsers(request):
    return render (request,'sponsers.html')