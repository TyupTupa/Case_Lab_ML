from django.urls import path
from .views import classification_form

urlpatterns = [
    path('', classification_form, name='classification_form'),
]
