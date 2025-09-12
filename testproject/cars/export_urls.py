from django.urls import path
from .export_views import export_data


urlpatterns = [
    path('', export_data, name='export-data'),
]
