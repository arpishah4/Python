from django import forms

class login(forms.form):
    username=forms.CharField(label="username",max_length=10)
    password=forms.CharField(label="password",max_length=10)