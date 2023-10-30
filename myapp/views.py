from django.shortcuts import render
from .models import MyProjectsModel

def index(request): 
    project = MyProjectsModel()
    project.id = 1
    project.name = "Note Project"
    project.detail = "Effortlessly capture your ideas, tasks, and memories with QuickNote - your sleek, intuitive note-taking companion. Simplify your life."
    project.url = "https://github.com/PhoenixIgris/NottoApp"
    project.image = "https://github.com/PhoenixIgris/NottoApp/blob/main/static/images/note.png?raw=true"    
    context = {"project": project}
    return render(request, 'index.html', context)
