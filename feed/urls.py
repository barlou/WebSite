from django.urls import URLPattern, path 
from feed.views import (
    index, 
)

app_name = 'feed'

urlpatterns = [
    path('', index, name="feed-home")
]
