from django import forms
from django.db.models import fields
from .models import books

#MAKE THE BOOK MODELFORM
class bookform(forms.ModelForm):
    class Meta:
        model=books
        fields= '__all__'