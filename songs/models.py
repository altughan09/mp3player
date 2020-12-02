import uuid
from django.db import models
from artists.models import Artist

class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_name')
    song_name = models.CharField(max_length=75)
    song_url = models.TextField()
    
    def __str__(self):
        return self.song_name


