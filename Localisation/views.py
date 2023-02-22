from django.shortcuts import render

def map_view(request):
    # Définissez la latitude et la longitude de la position que vous souhaitez afficher sur la carte
    # 42.705874532184495, 1.8401939751144654
    latitude = 42.705874532184495
    longitude = 1.8401939751144654

    context = {
        'latitude': latitude,
        'longitude': longitude,
    }

    return render(request, 'localisation.html', context)
