# bellapp/forms.py
from django import forms
from .models import BellSchedule

class BellScheduleForm(forms.ModelForm):
    class Meta:
        model = BellSchedule
        fields = ['time', 'day', 'audio_file']

class BulkEditAudioForm(forms.Form):
    new_audio_file = forms.FileField(label='New Audio File')
