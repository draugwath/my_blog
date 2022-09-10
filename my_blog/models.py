from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.Charfield
    image = models.ImageField(upload_to='post_images/')
