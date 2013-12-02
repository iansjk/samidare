from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('Nothing here but us trees!')
