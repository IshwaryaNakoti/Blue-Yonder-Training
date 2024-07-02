from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return HttpResponse("<h1>Hello Django</h1>")

def display(request):
    return HttpResponse("<h1>Display Django</h1>")

def displayHtml(request):
    return render(request, 'first.html')