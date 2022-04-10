
from django.db import models
from datetime import date
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=30)
    date = models.DateField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    slug = models.SlugField(default="",null=False)
    excerpt = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
  
    def save(self,*args,**kwargs): 
      self.slug = slugify(self.title)
      super().save(args,kwargs)

    def get_correct_slug(self):
      return reverse("dataPost",args=[self.slug])

    def __str__(self):
      return "author = {} and  title = {}".format(self.author,self.title)
