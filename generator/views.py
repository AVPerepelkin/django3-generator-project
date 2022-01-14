import requests
from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'generator/home.html', {'password':'bhiuhnmnb23212'})

def about(request):
    return render(request,'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('nambers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html', {'password': thepassword})