import uuid
from django.db import models
from genres.models import Genre

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name='genre_name')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
