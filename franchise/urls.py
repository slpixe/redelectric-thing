from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="franchise"),
    path('create/', views.franchise_create, name="create"),
    path('<slug:franchise_slug>', views.franchise_details,),
]
