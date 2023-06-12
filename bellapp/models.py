# schoolbell/bellapp/models.py
import os
from django.db import models

class BellSchedule(models.Model):
    DAY_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    )

    time = models.TimeField()
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)
    default_audio_file = models.FileField(upload_to='audio/', blank=True, null=True)

    def delete(self, *args, **kwargs):
        # Delete the associated audio file when deleting the bell schedule
        if self.audio_file:
            os.remove(self.audio_file.path)
        super().delete(*args, **kwargs)

    def reset_audio_file(self):
        self.audio_file = self.default_audio_file
        self.save()
