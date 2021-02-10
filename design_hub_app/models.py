from django.db import models
from django.forms import ModelForm
from django.shortcuts import redirect



class Guest(models.Model):
    id_number = models.CharField(max_length=12, blank=True)
    name = models.CharField(max_length=55)
    temperature = models.DecimalField(max_digits=3,decimal_places=1) 
    company = models.CharField(max_length=95)
    telephone_number = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class GuestForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Guest
        exclude = ['id']

   