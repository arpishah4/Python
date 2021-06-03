from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>WELCOME TO THE INDEX PAGE OF FIRTSTAPPLICATION!</h2>")

def first(request):
    return render(request,"first.html")
