from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Would you like to know more? I doubt it, there's really not much more to know.")

def subpage(request):
    return HttpResponse("this subpage is useful.")

def dogpage(request):
    return HttpResponse("ruff ruff! request={}".format(request))