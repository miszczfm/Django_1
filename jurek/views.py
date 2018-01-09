from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Name
import time

# Create your views here.
def post_list(request):
    naming = Name.objects.all()
    czas = time.localtime()
    return render(request, 'blog/name_list.html', {'naming': naming, 'czas': czas})

def time_return(request):
    czas = time.localtime()
    weekTime = round(czas.tm_yday/7)
    return render(request, 'blog/name_list.html', {'weekTime': weekTime})



