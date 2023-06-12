from django.shortcuts import render, redirect
from django.views import View
from .forms import BellScheduleForm, BulkEditAudioForm
from .models import BellSchedule, AudioFile, DayOfWeek

class BellScheduleView(View):
    def get(self, request):
        form = BellScheduleForm()
        audio_files = AudioFile.objects.all()
        days = DayOfWeek.objects.all()
        context = {
            'form': form,
            'audio_files': audio_files,
            'days': days,
        }
        return render(request, 'bellapp/bell_schedule.html', context)

    def post(self, request):
        form = BellScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bell_schedule')
        audio_files = AudioFile.objects.all()
        days = DayOfWeek.objects.all()
        context = {
            'form': form,
            'audio_files': audio_files,
            'days': days,
        }
        return render(request, 'bellapp/bell_schedule.html', context)

def delete_bell_schedule(request, pk):
    schedule = BellSchedule.objects.get(pk=pk)
    schedule.delete()
    return redirect('bell_schedule')

def delete_audio_file(request, pk):
    audio_file = AudioFile.objects.get(pk=pk)
    audio_file.delete()
    return redirect('bell_schedule')

def bulk_edit_audio(request):
    if request.method == 'POST':
        form = BulkEditAudioForm(request.POST)
        if form.is_valid():
            selected_audio = form.cleaned_data['selected_audio']
            schedules = BellSchedule.objects.all()
            for schedule in schedules:
                schedule.audio_file = selected_audio
                schedule.save()
            return redirect('bell_schedule')
    else:
        form = BulkEditAudioForm()
    audio_files = AudioFile.objects.all()
    context = {
        'form': form,
        'audio_files': audio_files,
    }
    return render(request, 'bellapp/bulk_edit_audio.html', context)
