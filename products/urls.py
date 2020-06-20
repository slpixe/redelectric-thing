from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('james/', views.james),
    path('stephen/', views.stephen)
]