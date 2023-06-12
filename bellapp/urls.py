# schoolbell/bellapp/urls.py
from django.urls import path
from .views import BellScheduleView, delete_bell_schedule, delete_audio_file, reset_audio_files, bulk_edit_audio

urlpatterns = [
    path('', BellScheduleView.as_view(), name='bell_schedule'),
    path('delete/<int:pk>/', delete_bell_schedule, name='delete_bell_schedule'),
    path('delete-audio/<int:pk>/', delete_audio_file, name='delete_audio_file'),
    path('reset-audio-files/', reset_audio_files, name='reset_audio_files'),
    path('bulk-edit-audio/', bulk_edit_audio, name='bulk_edit_audio'),
]
