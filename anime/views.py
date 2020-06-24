# from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Franchise, FranchiseItem
from . import forms
from django.contrib.auth.decorators import login_required

# def index(request):
#     return HttpResponse("Hello")

def index(request):
    franchises = Franchise.objects.all()
    franchiseitems = FranchiseItem.objects.all()
    return render(request, 'anime.html', {'franchises': franchises,'franchiseitems': franchiseitems,})


def franchise_details(request,franchise_slug):
    # return HttpResponse(franchise_slug)
    franchises_details = Franchise.objects.get(franchise_slug=franchise_slug)
    return render(request, 'franchises_details.html', {'franchises_details': franchises_details})

@login_required(login_url="/signup/login")
def franchise_create(request):
    if request.method == 'POST':
        form = forms.CreateFranchise(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            form_save = form.save(commit=False)
            form_save.author = request.user
            form_save.save()
            return redirect('anime')
    else:
        form = forms.CreateFranchise()
    return render(request, 'franchise_create.html', {'form': form})