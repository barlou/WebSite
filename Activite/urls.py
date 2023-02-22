from django.urls import URLPattern, path 
from Activite.views import (
    activite, 
)

app_name = 'Activite'

urlpatterns = [
    path('', activite, name="activities")
]
