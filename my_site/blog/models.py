from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=100)
    
    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    date = models.DateTimeField(auto_now=True)    
    image = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(4)])    
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="post")
    url = models.SlugField(unique=True, default="", null=False) # unique filed automatically index=True
    tag = models.ManyToManyField(Tag)
    

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super().save(*args, **kwargs)

    def post_name(self):
        return f"{self.title}"
        
    def __str__(self):
        return self.post_name()

