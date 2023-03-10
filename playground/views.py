from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from requests import Response


# Create your views here.

def foo(request: HttpRequest):
    return HttpResponse(content_type='application/json')

