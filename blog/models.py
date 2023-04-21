from django.db import models
from datetime import datetime
from authors.models import Author
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    post_intro = models.CharField(max_length=500)
    post_sneakpeak = models.TextField()
    post_main = models.TextField()
    is_published = models.BooleanField(default=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    
    class Meta:
        ordering = ['date_added']
    
   
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
