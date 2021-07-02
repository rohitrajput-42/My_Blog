from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Categories(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        #return reverse('article-detail', args = (str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length = 10000)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length = 200, default = "movies-tvshows")

    def __str__(self):
        return f"{self.title}  |  By - {self.author}"

    def get_absolute_url(self):
        #return reverse('article-detail', args = (str(self.id)))
        return reverse('home')