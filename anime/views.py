# from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Franchise, FranchiseItem, FranchiseUser, FranchiseItemUser
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from slugify import slugify

# def index(request):
#     return HttpResponse("Hello")

@login_required(login_url="/signup/login")
def index(request):
    franchises = Franchise.objects.all()
    franchiseitems = FranchiseItem.objects.all()
    return render(request, 'anime.html', {'franchises': franchises,'franchiseitems': franchiseitems,})

@login_required(login_url="/signup/login")
def franchise_details(request,franchise_slug):    
    franchises_details = Franchise.objects.get(franchise_slug=franchise_slug)
    

    #Franchise items opinion items VVVV 
    try:
        franchise_items_films = FranchiseItem.objects.filter(franchies_name=franchises_details.id,area_type="Film")
        
    except:
        franchise_items_films = None
    try:
        franchise_items_tvs = FranchiseItem.objects.filter(franchies_name=franchises_details.id,area_type="TV")
    except:
        franchise_items_tvs = None
    #Franchise items opinion items ^^^^^^

    #User opinion items VVVV 
    franchise_item_users_film = FranchiseItemUser.objects.filter(franchies_name=franchises_details.id, author=request.user, area_type="Film")
    if not franchise_item_users_film.exists():
        franchise_item_users_film = None
    
    franchise_item_users_tv = FranchiseItemUser.objects.filter(franchies_name=franchises_details.id, author=request.user, area_type="TV")
    if not franchise_item_users_tv.exists():
        franchise_item_users_tv = None
        
    #User opinion items ^^^^^^
    try:
        franchises_user = FranchiseUser.objects.get(franchies_name=franchises_details.id, author=request.user)
    except:
        franchises_user = None    
    return render(request, 'franchises_details.html', {'franchises_details': franchises_details, 'franchises_user': franchises_user, 'franchise_items_films':franchise_items_films, 'franchise_items_tvs':franchise_items_tvs,'franchise_item_users_film':franchise_item_users_film,'franchise_item_users_tv':franchise_item_users_tv})


@staff_member_required(login_url="/signup/login")
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

def franchise_item_create(request,franchise_slug):
    franchises_details = Franchise.objects.get(franchise_slug=franchise_slug)
    if request.method == 'POST':
        form = forms.CreateFranchiseItem(request.POST)
    else:       
        form = forms.CreateFranchiseItem()
    return render(request, 'franchise_item_create.html',{'franchises_details':franchises_details,'form':form})