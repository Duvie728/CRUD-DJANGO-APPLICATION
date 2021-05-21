from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



class Comment(models.Model):
    post = models.ForeignKey(
        Post,
         on_delete=models.CASCADE,
         related_name='comments',
        
    ) 
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
            'auth.User',
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        #return '%s - %s' % (self.post.title, self.comment)
        return self.comment


    def get_absolute_url(self):
        return reverse('post:post_detail', args=[str(self.post.pk)])