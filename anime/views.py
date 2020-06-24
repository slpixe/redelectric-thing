# from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Franchise, FranchiseItem
from . import forms
from django.contrib.auth.decorators import login_required
from slugify import slugify

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
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.franchise_slug = slugify(form_instance.franchies_name)
            form_instance.all_user_average = 0
            # This is for working out what franchise types their are VVVV
            if form_instance.film_num > 0:
                form_instance.film_type = True
            else:
                form_instance.film_type = False
            if form_instance.tv_num > 0:
                form_instance.tv_type = True
            else:
                form_instance.tv_type = False
            if form_instance.oav_num > 0:
                form_instance.oav_type = True
            else:
                form_instance.oav_type = False
            # This is for working out what franchise types their are ^^^^
            form_instance.save()
            return redirect('anime')
    else:
        form = forms.CreateFranchise()
    return render(request, 'franchise_create.html', {'form': form})