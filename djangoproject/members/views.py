from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Members

def login(request):
    return render(request,'login.html',{})

def loginsuccess(request):
    x = request.POST['username']
    y= request.POST['password']

    if x == 'Karan' and y == 'Admin':
        mymembers = Members.objects.all().values()
        context = {
            'mymembers':mymembers,
        }
        return render(request,'index.html',context)
    else:
        return redirect('login')
# def index(request):
#      mymembers = Members.objects.all().values()
#      context = {
#         'mymembers':mymembers,
#      }
#      return render(request,'index.html',context)

def add(request):
    return render(request,'add.html',{})

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return redirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return redirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request,'update.html',context)

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return redirect(reverse('index'))
# Create your views here.
