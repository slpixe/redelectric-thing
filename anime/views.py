# from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Franchise, FranchiseItem, FranchiseUser, FranchiseItemUser
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from slugify import slugify

# def index(request):
#     return HttpResponse("Hello")


class Item:
    def __init__(self, name, story, animation, music, overall):
        self.name = name
        self.story = story
        self.animation = animation
        self.music = music
        self.overall = overall

class Ep:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate



@login_required(login_url="/signup/login")
def index(request):
    franchises = Franchise.objects.all()
    franchiseitems = FranchiseItem.objects.all()
    return render(request, 'anime.html', {'franchises': franchises, 'franchiseitems': franchiseitems, })


@login_required(login_url="/signup/login")
def franchise_details(request, franchise_slug):
    franchises_details = Franchise.objects.get(franchise_slug=franchise_slug)
    form_type = forms.CreateFranchiseItemEp
    if request.method == 'POST':
        if "Film" in request.POST:
            area = "Film"
            form_type = forms.CreateFranchiseItemNoEp
        if "TV" in request.POST:
            area = "TV"
            form_type = forms.CreateFranchiseItemEp
        if "OAV" in request.POST:
            area = "OAV"
            form_type = forms.CreateFranchiseItemEp
        form = form_type(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.franchies_name_id = franchises_details.id
            form_instance.area_type = area
            if area == "Film":
                form_instance.number_of_episodes = 0
            form_instance.all_user_average = 0
            form_instance.save()
            return redirect('/' + franchises_details.franchise_slug)
    else:
        form = form_type()
        area = ""

        films = []
        franchise_items_films = FranchiseItem.objects.filter(franchies_name=franchises_details.id, area_type="Film")            
        if not franchise_items_films.exists():
            films = None
        else:
            franchise_item_users_film = FranchiseItemUser.objects.filter(franchies_name=franchises_details.id, author=request.user, area_type="Film")
            for film_item in franchise_items_films:
                rating = False
                for film_rate in franchise_item_users_film:
                    if film_item.id == film_rate.franchies_item_name_id:
                        rating = True
                        film_item.stroy = film_rate.story_opinion
                        film_item.animation = film_rate.animation_opinion
                        film_item.music = film_rate.music_opinion
                        film_item.overall = film_rate.user_opinion_average
                if rating == False:
                    film_item.stroy = "Not Yet Rated"
                    film_item.animation = "Not Yet Rated"
                    film_item.music = "Not Yet Rated"
                    film_item.overall = "Not Yet Rated"
                films.append( Item(film_item.name, film_item.stroy, film_item.animation, film_item.music, film_item.overall))           

        TVS = []
        # Franchise items opinion items VVVV
        try:
            franchise_items_tvs = FranchiseItem.objects.filter(
                franchies_name=franchises_details.id, area_type="TV")
        except:
            franchise_items_tvs = None
        # Franchise items opinion items ^^^^^^

        # User opinion items VVVV
        franchise_item_users_tv = FranchiseItemUser.objects.filter(
            franchies_name=franchises_details.id, author=request.user, area_type="TV")
        franchise_item_users_tv_num = franchise_item_users_tv.count()
        if not franchise_item_users_tv.exists():
            franchise_item_users_tv = None
            franchise_item_users_tv_num = 0

        # User opinion items ^^^^^^
        try:
            franchises_user = FranchiseUser.objects.get(
                franchies_name=franchises_details.id, author=request.user)
        except:
            franchises_user = None

    return render(request, 'franchises_details.html', {'franchises_details': franchises_details, 'franchises_user': franchises_user, 'franchise_items_tvs': franchise_items_tvs, 'franchise_item_users_tv': franchise_item_users_tv, 'form': form, 'area': area, 'franchise_item_users_tv_num': franchise_item_users_tv_num, "films":films})


@staff_member_required(login_url="/signup/login")
def franchise_create(request):
    if request.method == 'POST':
        form = forms.CreateFranchise(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.franchise_slug = slugify(
                form_instance.franchies_name)
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
