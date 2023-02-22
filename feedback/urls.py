from django.urls import URLPattern, path 
from feedback.views import (
    index, 
)

app_name = 'feedback'

urlpatterns = [
    path('', index, name="feedback-home")
]
