from django.contrib import admin
from . models import Franchise, FranchiseUser, FranchiseItem, Episides, Music, FranchiseItemUser


class FranchiseAdmin(admin.ModelAdmin):
    list_display = ('franchies_name',)


class FranchiseUserAdmin(admin.ModelAdmin):
    list_display = ('franchies_name',)

class FranchiseItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'franchies_name',)


class EpisidesAdmin(admin.ModelAdmin):
    list_display = ('franchies_name',)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('song_name',)

class FranchiseItemUserAdmin(admin.ModelAdmin):
    list_display = ('franchies_item_name', 'franchies_name',)

admin.site.register(Franchise, FranchiseAdmin)
admin.site.register(FranchiseUser, FranchiseUserAdmin)
admin.site.register(FranchiseItem, FranchiseItemAdmin)
admin.site.register(Episides, EpisidesAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(FranchiseItemUser, FranchiseItemUserAdmin)
