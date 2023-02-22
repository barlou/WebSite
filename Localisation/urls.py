from django.urls import URLPattern, path 
from .views import map_view

app_name = 'Localisation'


urlpatterns = [
   path('', map_view, name="localisation")
]
