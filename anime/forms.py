from django import forms
from . import models

class CreateFranchise(forms.ModelForm):
    class Meta:
        model = models.Franchise
        fields = ["franchies_name", "franchise_slug", "thumb", "film_type", "film_num", "tv_type", "tv_num", "oav_type", "oav_num", "all_user_average"]