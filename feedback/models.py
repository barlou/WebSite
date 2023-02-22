from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Comment_location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
class Comment_site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
admin.site.register(Comment_site)
admin.site.register(Comment_location)