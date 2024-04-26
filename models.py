from django.db import models
from Bloguser.models import CustomUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(blank=True)

    class Meta:
        verbose_name_plural='Categories'


    def __str__(self) -> str:
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    publication_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to='thumbnails')


    def __str__(self) -> str:
        return f'{self.title}'