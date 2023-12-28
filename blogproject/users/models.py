from django.db import models

# Create your models here.

class AddUser(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.email}"