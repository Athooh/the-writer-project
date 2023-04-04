from django.db import models
from datetime import datetime
from authors.models import Author

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    post_intro = models.CharField(max_length=500)
    post_main = models.TextField()
    is_published = models.BooleanField(default=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title