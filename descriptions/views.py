from django.shortcuts import render
from django.http import HttpResponse

def descPageView(request) :
    return HttpResponse('Recipe Description Page')  

def editPageView(request) :
    return HttpResponse('Edit Recipies Here')

def addPageView(request) :
    return HttpResponse('This is where one would hypothetically add a recipe...')