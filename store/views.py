from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text_bar = 'A shopping Cart By Prasoon'
    return HttpResponse(text_bar)
