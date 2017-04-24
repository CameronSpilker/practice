from django.db import models

# Create your models here.

class Category(models.Model):
    #id
    author = models.TextField(blank=True, null=True, unique=True)
    quote = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.name
