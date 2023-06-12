# bellapp/models.py
from django.db import models

class BellSchedule(models.Model):
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    ]

    time = models.TimeField()
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)

    def reset_audio_file(self):
        self.audio_file = None
        self.save()

    def __str__(self):
        return f'{self.get_day_display()} - {self.time}'
