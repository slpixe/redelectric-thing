from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="anime"),
    path('create/', views.franchise_create, name="create"),
    path('<slug:franchise_slug>', views.franchise_details,),
    path('<slug:franchise_slug>/film', views.franchise_item_create_film,),
    path('<slug:franchise_slug>/tv', views.franchise_item_create_tv,),
    path('<slug:franchise_slug>/oav', views.franchise_item_create_oav,),
]
