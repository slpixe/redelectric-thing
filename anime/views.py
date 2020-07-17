# from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Franchise, FranchiseItem, FranchiseUser, FranchiseItemUser, Episides, EpisidesUser
from . import forms
from django.db.models import Count,Prefetch, prefetch_related_objects
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from slugify import slugify

# def index(request):
#     return HttpResponse("Hello")

rate_max = str("/5")

print('START!!!!!!!!!!!!!!!')
class Episode:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

class Item:
    def __init__(self, name, ep_num, story, animation, music, overall,ep_sets):
        self.name = name
        self.ep_num = ep_num
        self.story = story
        self.animation = animation
        self.music = music
        self.overall = overall
        episode_list = []
        ep_items = 0
        self.ep_sets = ep_sets
        if self.ep_sets != None:
            for ep_set in self.ep_sets:
                ep_items = 1
                name = ep_set.episode_number
                rate = "Not Yet Rated"
                for ep_rate in ep_set.episidesuser_set.all():
                    rate = (f'{ep_rate.user_opinion}{rate_max}')                
                episode_list.append(Episode(name,rate))
        self.ep_items = ep_items
        self.episode_list = episode_list
        


        


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

        # Film code VVVVV
        films = []
        film_items = FranchiseItem.objects.filter(franchies_name=franchises_details.id, area_type="Film")
        if not film_items.exists():
            films = None
        else:
            film_rates = FranchiseItemUser.objects.filter(franchies_name=franchises_details.id, author=request.user, area_type="Film")
            for film_item in film_items:
                film_rating = False
                for film_rate in film_rates:
                    if film_item.id == film_rate.franchies_item_name_id:
                        film_rating = True
                        film_item.stroy = (f'{film_rate.story_opinion}{rate_max}')
                        film_item.animation = (f'{film_rate.animation_opinion}{rate_max}')
                        film_item.music = (f'{film_rate.music_opinion}{rate_max}')
                        film_item.overall = (f'{film_rate.user_opinion_average}{rate_max}')
                if not film_rating:
                    film_item.stroy = "Not Yet Rated"
                    film_item.animation = "Not Yet Rated"
                    film_item.music = "Not Yet Rated"
                    film_item.overall = "Not Yet Rated"
                films.append(Item(film_item.name, 0, film_item.stroy, film_item.animation, film_item.music, film_item.overall,None))
        # Film code ^^^^^
        # TV code VVVVV
        tvs = FranchiseItem.objects.filter(franchies_name=franchises_details.id, area_type="TV").prefetch_related(
            Prefetch(
                'franchiseitemuser_set',
                queryset=FranchiseItemUser.objects.filter(author=request.user)
                )
            ).prefetch_related(
            Prefetch(
                'episides_set',
                queryset=Episides.objects.all()
                )
            ).prefetch_related(
            Prefetch(
                'episidesuser_set',
                queryset=EpisidesUser.objects.all()
                )
            ).all()
        tv_list = []
        
        for tv_item in tvs:
            tv_item.stroy = "Not Yet Rated"
            tv_item.animation = "Not Yet Rated"
            tv_item.music = "Not Yet Rated"
            tv_item.overall = "Not Yet Rated"
            for tv_rate in tv_item.franchiseitemuser_set.all():
                tv_item.stroy = (f'{tv_rate.story_opinion}{rate_max}')
                tv_item.animation = (f'{tv_rate.animation_opinion}{rate_max}')
                tv_item.music = (f'{tv_rate.music_opinion}{rate_max}')
                tv_item.overall = (f'{tv_rate.user_opinion_average}{rate_max}')
            tv_list.append(Item(tv_item.name,0,tv_item.stroy,tv_item.animation,tv_item.music,tv_item.overall,tv_item.episides_set.all()))
        # TV code ^^^^^
        try:
            franchises_user = FranchiseUser.objects.get(
                franchies_name=franchises_details.id, author=request.user)
        except:
            franchises_user = None

    compinants = {
        'franchises_details': franchises_details, 
        'franchises_user': franchises_user,
        'form': form,
        'area': area,
        "films":films,
        "tvs":tvs,
        "tv_list":tv_list
    }

    return render(request, 'franchises_details.html', compinants)


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
