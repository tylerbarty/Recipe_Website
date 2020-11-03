from django.urls import path
from django.http import HttpResponse
from .views import indexPageView

urlpatterns = [
    path("", indexPageView, name="index")    
]   