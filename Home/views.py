from django.shortcuts import render 

def index(request):
    return render(request, "Home/templates/index.html") 
