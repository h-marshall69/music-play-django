from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    audiofile = models.FileField()
    listens = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='music_covers/', null=True, blank=True)

    def __str__(self):
        return self.title + ": " + str(self.audiofile)
    
    class Meta:
        ordering = ['listens', 'date_added']
