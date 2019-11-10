from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    name = request.GET.get('name')
    return HttpResponse("Hello, %s. You're at the polls index." % name)


def lists(request):
    return HttpResponse("Polls list is coming soon here...")
