from django import forms
from .models import *

class AppForm(forms.ModelForm):
    
    class Meta:
        model = App
        fields = ('name', 'description', 'icon', 'privacy', 'tutorial', 'url', 'price', 'support', 'testimonial', 'functions', 'formats', 'types',)

class FormatForm(forms.ModelForm):

    class Meta:
        model = Format
        fields = ('name',)

class FunctionForm(forms.ModelForm):

    class Meta:
        model = Function
        fields =('name',)

class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ('name',)
