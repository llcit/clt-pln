from django import forms
from .models import *

class AppForm(forms.ModelForm):

    class Meta:
        model = App
        fields = ('name', 'description', 'icon', 'privacy', 'tutorial', 'url', 'testimonial', 'applications', 'formats', 'functions', 'price', 'support', )

class FormatForm(forms.ModelForm):

    class Meta:
        model = Format
        fields = ('name',)

class FunctionForm(forms.ModelForm):

    class Meta:
        model = Function
        fields =('name',)

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name',)
