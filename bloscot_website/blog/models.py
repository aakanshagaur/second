from django.db import models
from users.models import AddUser

# Create your models here.


class AddBlog(models.Model):
    
    author = models.ForeignKey(to=AddUser, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    post = models.TextField(max_length = 1000)
    category = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.author}"