from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    duration_minutes = models.IntegerField(null=True, blank=True)
    is_blockbuster = models.BooleanField(default=False)

    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='added_movies',
        null=True,        # allow nulls for now
        blank=True        # allow blank in admin/forms
    )

    def __str__(self):
        return f"{self.title} ({self.release_year})"