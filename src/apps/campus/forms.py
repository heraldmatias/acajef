from django import forms
from models import Campus

"""
Simple ModelForm for Campus
"""

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
