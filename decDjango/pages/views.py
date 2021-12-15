from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> This is Home Page </h1>")