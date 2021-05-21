from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    model =  User #Comment
    fields = ['comment']
    widgets = { 'body': forms.Textarea(attrs={'class':'form-control'})}