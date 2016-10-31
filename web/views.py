from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('index.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
