from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('appointment-list/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointment/<int:pk>', AppointDetailView.as_view(), name='appointment'),
    path('client-list/', ClientDetailView.as_view(), name='client-list'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client'),
]

