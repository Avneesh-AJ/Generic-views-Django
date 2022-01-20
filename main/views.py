from configparser import InterpolationDepthError
from dataclasses import field
from pydoc import ModuleScanner
from re import template
from sre_constants import SUCCESS
from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main import models
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

#def index(request):
    #return render(request,'index.html')


class Index(ListView):
    model=models.College
    template_name='index.html'
    

class CollegeDetail(DetailView):
    model=models.College
    template_name='College_detail.html'


class CollegeList(ListView):
    model=models.College
    template_name='College_list.html'
    context_object_name='colleges'


class CollegeCreate(CreateView):
    model=models.College
    template_name="College_create.html"
    fields="__all__"
    success_url="/colleges"

class CollegeUpdate(UpdateView):
    model=models.College
    template_name="College_create.html"
    fields="__all__"
    success_url="/colleges"


class StudentCreate(CreateView):
    model=models.Student
    template_name="Student_create.html"
    success_url="/colleges"
    fields="__all__"


class StudentUpdate(UpdateView):
    model=models.Student
    template_name="Student_create.html"
    success_url="/colleges"
    fields="__all__"


class StudentDelete(DeleteView):
    model=models.Student
    template_name="delete.html"
    success_url="/colleges"
    


