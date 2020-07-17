from django.contrib import admin
from . models import Franchise, FranchiseUser, FranchiseItem, Episides, Music, FranchiseItemUser, EpisidesUser


class FranchiseAdmin(admin.ModelAdmin):
    list_display = ('franchies_name',)


class FranchiseUserAdmin(admin.ModelAdmin):
    list_display = ('franchies_name',)

class FranchiseItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'franchies_name',)


class EpisidesAdmin(admin.ModelAdmin):
    list_display = ('franchies_name', 'franchies_item_name', 'episode_number',)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('song_name',)

class FranchiseItemUserAdmin(admin.ModelAdmin):
    list_display = ('franchies_item_name', 'franchies_name',)

class EpisidesUserAdmin(admin.ModelAdmin):
    list_display = ('franchies_name', 'franchies_item_name', 'episode_number', 'author',)

admin.site.register(Franchise, FranchiseAdmin)
admin.site.register(FranchiseUser, FranchiseUserAdmin)
admin.site.register(FranchiseItem, FranchiseItemAdmin)
admin.site.register(Episides, EpisidesAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(FranchiseItemUser, FranchiseItemUserAdmin)
admin.site.register(EpisidesUser, EpisidesUserAdmin)
