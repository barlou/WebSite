from django import forms
from feedback.models import Comment_site, Comment_location

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class CommentLocationForm(forms.ModelForm):
        
    text = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Votre commentaire',
            'rows': 4,
            'cols': 50,    
        }))
    
    rating = forms.ChoiceField(choices=RATING_CHOICES, label="Note")
    
    class Meta:
        # J'ai pas de rating 
        model = Comment_location
        fields = ('text', 'rating')
    
    
class CommentSiteForm(forms.ModelForm):
    
    text = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder' : 'Votre commentaire',
            'rows':4,
            'cols':50,
        }
    ))
    
    rating = forms.ChoiceField(choices=RATING_CHOICES, label="Note")
    
    class Meta:
        model = Comment_site 
        fields = ('text', 'rating')