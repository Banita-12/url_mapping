from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('Hi, How r U')

def jigalrani(request):
    return HttpResponse('I m good')