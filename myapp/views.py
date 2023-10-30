from django.shortcuts import render
from .models import MyProjectsModel


def index(request):
    myprojects = MyProjectsModel.objects.all()
    return render(request, 'index.html', {'projects': myprojects})
