from django.urls import path
from .views import BellScheduleView, delete_bell_schedule, delete_audio_file, bulk_edit_audio

urlpatterns = [
    path('', BellScheduleView.as_view(), name='bell_schedule'),
    path('delete/<int:pk>/', delete_bell_schedule, name='delete_bell_schedule'),
    path('delete_audio/<int:pk>/', delete_audio_file, name='delete_audio_file'),
    path('bulk_edit_audio/', bulk_edit_audio, name='bulk_edit_audio'),
]
