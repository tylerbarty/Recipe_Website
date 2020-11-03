from django.urls import path
from .views import descPageView
from .views import editPageView
from .views import addPageView

urlpatterns = [
    path("desc", descPageView, name="Description"),
    path("desc/edit", editPageView, name="edit"),
    path("desc/add", addPageView, name="add")  
]   