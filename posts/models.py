from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class Post(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField(blank=True, max_length=140 )
    time = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['time']

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('posts:index.html', args={'id': self.pk})




