from django.urls import path
from apps.dashboard import views

urlpatterns = [
path('dashboard/',views.dashboard_index,name='dashboard-view')
]