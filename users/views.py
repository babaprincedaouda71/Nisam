from django.shortcuts import render
from .models import Background
import io
from django.http import FileResponse
# from reportlab.pdfgen import canvas

from activities.models import Activitie

def base(request):
    return render(request, 'users/base.html')

def index(request):
    # images = Background.objects.all()
    activities = Activitie.objects.all()
    return render(request, 'users/index.html', {'activities' : activities})

def more(request):
    return render(request, 'users/more.html')

def formations(request):
    return render(request, 'users/formations.html')

