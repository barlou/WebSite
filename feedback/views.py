from django.shortcuts import render, redirect
from feedback.form import CommentSiteForm, CommentLocationForm
from feedback.models import Comment_site, Comment_location
# SQlite ne connait pas la fonction Round, je ne peux pas arrondir aux dixième
from django.db.models import Avg

def index(request):
    comments = Comment_site.objects.order_by('-rating')
    comments_location = Comment_location.objects.order_by('-rating')
    form = CommentSiteForm()
    form_location = CommentLocationForm()
    rating = Comment_site.objects.aggregate(Avg('rating'))['rating__avg']
    rating_location = Comment_location.objects.aggregate(Avg('rating'))['rating__avg']
    
    if request.user.is_authenticated:
        if request.method == "POST":
                form = CommentSiteForm(request.POST)
                form_location = CommentLocationForm(request.POST)
                form_type = request.POST.get('form_type')
                if form_type =="location":
                    if form_location.is_valid():
                        comment_location = form_location.save(commit=False)
                        comment_location.user = request.user
                        comment_location.save()
                        return redirect('feedback:feedback-home')
                elif form_type == "site":
                    if form.is_valid():
                        comment = form.save(commit=False)
                        comment.user = request.user
                        comment.save()
                        return redirect('feedback:feedback-home')
    else:
        return redirect('Login:login-login')
    
    context = {'form':form, 
               'form_location': form_location,
               'comments':comments, 
               'comments_location':comments_location, 
               'avg_rating_site' : rating, 
               'avg_rating_location' : rating_location}
    
    return render(request, "feedback/templates/index.html", context)
