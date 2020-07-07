from django import forms
from . import models

class CreateFranchise(forms.ModelForm):
    class Meta:
        model = models.Franchise
        fields = ["franchies_name", "thumb", "film_num", "tv_num", "oav_num",]

        widgets = {
            "franchies_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name of Franchise"}),
            "thumb": forms.FileInput(attrs={'class': 'form-control-file'}),
            "film_num": forms.NumberInput(attrs={'class': 'form-control'}),
            "tv_num": forms.NumberInput(attrs={'class': 'form-control'}),
            "oav_num": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CreateFranchiseItemNoEp(forms.ModelForm):
    class Meta:
        model = models.FranchiseItem
        fields = ["name",]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Item Name"}),
        }


class CreateFranchiseItemEp(forms.ModelForm):
    class Meta:
        model = models.FranchiseItem
        fields = ["name","number_of_episodes",]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Item Name"}),
            "number_of_episodes": forms.NumberInput(attrs={'class': 'form-control'}),
        }
