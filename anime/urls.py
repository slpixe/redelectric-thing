from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="anime"),
    path('<slug:franchise_slug>', views.franchise_details,),
]
