from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts:index.html', args={'id': self.pk})