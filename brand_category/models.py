from django.db import models
from datetime import datetime
from authors.models import Author

# Create your models here.
class Brands(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    brand_intro = models.CharField(max_length=400)
    brand_description = models.TextField()
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title