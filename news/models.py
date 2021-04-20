from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=300)
    date_published = models.DateTimeField()
    content = models.CharField(max_length=1000)

