from django import forms
from . import models

class CreateFranchise(forms.ModelForm):
    class Meta:
        model = models.Franchise
        fields = ["franchies_name", "franchise_slug", "thumb", "film_type", "film_num", "tv_type", "tv_num", "oav_type", "oav_num", "all_user_average"]

        widgets = {
            "franchies_name": forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Name of Franchise"}),
            "franchise_slug": forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Slug Name"}),
            "thumb": forms.FileInput(attrs={'class': 'form-control-file'}),
            "film_type": forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            "film_num": forms.NumberInput(attrs={'class': 'form-control'}),
            "tv_type": forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            "tv_num": forms.NumberInput(attrs={'class': 'form-control'}),
            "oav_type": forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            "oav_num": forms.NumberInput(attrs={'class': 'form-control'}),
            "all_user_average": forms.NumberInput(attrs={'class': 'form-control'}),
        }