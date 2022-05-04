from django.db import models

# Create your models here.
class Todo (models.Model):
    title = models.CharField(max_length=100)    

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=500)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title