from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    date = models.DateTimeField(auto_now_add=True)    
    image = models.CharField(max_length=100)
    content = models.TextField()    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="post")
    url = models.SlugField(default="", null=False, db_index=True)
    

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super().save(*args, **kwargs)

    def post_name(self):
        return f"{self.title}"
        
    def __str__(self):
        return self.post_name()