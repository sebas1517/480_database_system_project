from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # if request.method == 'POST':
    #     username = request.post['username']
    #     password = request.post['password']

    return render(request, 'home.html', {})
