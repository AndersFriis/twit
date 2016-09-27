from django.db import models

# Create your models here.

class Post (models.Model):
    title=models.CharField(max_length=200)
    publish_date=models.DateTimeField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)   