from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Application(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Format(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Function(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Price(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Support(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    icon_image = models.ImageField(upload_to='pln/static/images/icon', null=True, blank=True)
    privacy = models.CharField(max_length=255, null=True, blank=True)
    tutorial = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    testimonial = models.CharField(max_length=255, null=True, blank=True)
    application = models.ManyToManyField(Application)
    format = models.ManyToManyField(Format)
    function = models.ManyToManyField(Function)
    price = models.ManyToManyField(Price)
    support = models.ManyToManyField(Support)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
