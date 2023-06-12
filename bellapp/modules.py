# schoolbell/bellapp/models.py
import os
from django.db import models

class BellSchedule(models.Model):
    time = models.TimeField()
    audio_file = models.FileField(upload_to='audio/')

    def delete(self, *args, **kwargs):
        # Delete the associated audio file when deleting the bell schedule
        if self.audio_file:
            os.remove(self.audio_file.path)
        super().delete(*args, **kwargs)

# schoolbell/bellapp/views.py
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import BellSchedule
from .forms import BellScheduleForm

class BellScheduleView(View):
    def get(self, request):
        bell_schedules = BellSchedule.objects.all()
        form = BellScheduleForm()
        return render(request, 'bellapp/bell_schedule.html', {'bell_schedules': bell_schedules, 'form': form})

    def post(self, request):
        form = BellScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'bellapp/bell_schedule.html', {'form': form})

def delete_bell_schedule(request, pk):
    bell_schedule = get_object_or_404(BellSchedule, pk=pk)
    bell_schedule.delete()
    return redirect('bell_schedule')

def delete_audio_file(request, pk):
    bell_schedule = get_object_or_404(BellSchedule, pk=pk)
    if bell_schedule.audio_file:
        os.remove(bell_schedule.audio_file.path)
        bell_schedule.audio_file = None
        bell_schedule.save()
    return redirect('bell_schedule')