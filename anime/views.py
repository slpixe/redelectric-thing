# from django.http import HttpResponse
from django.shortcuts import render
from . models import Franchise, FranchiseItem

# def index(request):
#     return HttpResponse("Hello")

def index(request):
    franchises = Franchise.objects.all()
    franchiseitems = FranchiseItem.objects.all()
    return render(request, 'anime.html', {'franchises': franchises,'franchiseitems': franchiseitems,})


def franchise_details(request,franchise_slug):
    # return HttpResponse(franchise_slug)
    franchises_details = Franchise.objects.get(franchise_slug=franchise_slug)
    return render(request, 'franchises_details.html',{'franchises_details': franchises_details})

def franchise_create(request):
    return render(request, 'franchise_create.html')