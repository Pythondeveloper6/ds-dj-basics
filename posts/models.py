from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , related_name='author_user')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='authors')
    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(Author , on_delete=models.CASCADE , related_name='post_author')
    tags = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    # title , content , image , author , tags 