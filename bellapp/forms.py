from django import forms
from .models import BellSchedule, AudioFile

class BellScheduleForm(forms.ModelForm):
    class Meta:
        model = BellSchedule
        fields = ['time', 'day', 'audio_file']

class BulkEditAudioForm(forms.Form):
    selected_audio = forms.ModelChoiceField(queryset=AudioFile.objects.all(), required=True, empty_label=None)
