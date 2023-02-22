from django.urls import URLPattern, path 
from presentation.views import (
    presentation, 
)

app_name = 'presentation'

urlpatterns = [
    path('', presentation, name="index")
]
