from django.shortcuts import render 

def presentation(request):
    return render(request, "presentation/templates/presentation.html") 
