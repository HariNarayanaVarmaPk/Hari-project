from django.db import models
from django.contrib.auth.models import User

class Cinema(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    trailer_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title
