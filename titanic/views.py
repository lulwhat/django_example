from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import titanic

def index(request):
    return render(request, "index.html")