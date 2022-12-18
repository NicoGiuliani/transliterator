from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transliterate', views.transliterate, name='transliterate')
]
