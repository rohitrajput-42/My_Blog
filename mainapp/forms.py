from django import forms
from .models import Post, Categories
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
            'password1': forms.TextInput(attrs = {'class': 'form-control'}),
            'password2': forms.TextInput(attrs = {'class': 'form-control'}),
        }



'''
choices = [('stock-market', 'stock-market'),
           ('news', 'news'),
           ('cooking', 'cooking'),
           ('sports', 'sports'),
           ('movies-tvshows', 'movies-tvshows')]
'''

choices = Categories.objects.all().values_list('name', 'name')
 
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs = {'class': 'form-control'}),
            'author': forms.Select(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
        } 



class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
        }