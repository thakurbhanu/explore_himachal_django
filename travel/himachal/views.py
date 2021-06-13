from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')




class BookListView(generic.ListView):
    model = place

class BookDetailView(generic.DetailView):
    model = place