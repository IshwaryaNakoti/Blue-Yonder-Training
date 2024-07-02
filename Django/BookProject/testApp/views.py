from typing import Any
from django.shortcuts import render
from testApp.models import Book
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<h1>Class based view</h1>")
    
class TemplateCBV(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = "BlueYonder"
        context['age'] = 45
        return context
    
# Create your views here. 
class BookListView(ListView): 
	model=Book

class BookCreateView(CreateView):
     model = Book
     fields = ['title','author','pages','price']

     