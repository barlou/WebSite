from django.urls import URLPattern, path 
from Home.views import (
    index, 
)

app_name = 'Home'

urlpatterns = [
    path('', index, name="Home-index")
]
