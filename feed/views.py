from django.shortcuts import render 

def index(request):
    return render(request, "feed/templates/feed.html") 
