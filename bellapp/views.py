# bellapp/views.py
from django.shortcuts import render, redirect
from django.views import View
from .models import BellSchedule
from .forms import BellScheduleForm, BulkEditAudioForm

class BellScheduleView(View):
    def get(self, request):
        schedules = BellSchedule.objects.order_by('day', 'time')
        form = BellScheduleForm()
        bulk_edit_form = BulkEditAudioForm()
        return render(request, 'bellapp/bell_schedule.html', {
            'schedules': schedules,
            'form': form,
            'bulk_edit_form': bulk_edit_form
        })

    def post(self, request):
        form = BellScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('bell_schedule')

def delete_bell_schedule(request, pk):
    schedule = BellSchedule.objects.get(pk=pk)
    schedule.delete()
    return redirect('bell_schedule')

def delete_audio_file(request, pk):
    schedule = BellSchedule.objects.get(pk=pk)
    if schedule.audio_file:
        schedule.audio_file.delete()
        schedule.reset_audio_file()
    return redirect('bell_schedule')

def reset_audio_files(request):
    schedules = BellSchedule.objects.all()
    for schedule in schedules:
        schedule.reset_audio_file()
    return redirect('bell_schedule')

def bulk_edit_audio(request):
    if request.method == 'POST':
        form = BulkEditAudioForm(request.POST, request.FILES)
        if form.is_valid():
            new_audio_file = form.cleaned_data['new_audio_file']
            schedules = BellSchedule.objects.all()
            for schedule in schedules:
                schedule.audio_file = new_audio_file
                schedule.save()
    return redirect('bell_schedule')
