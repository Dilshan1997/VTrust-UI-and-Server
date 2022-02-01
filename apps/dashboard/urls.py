from django.urls import path
from apps.dashboard import views

urlpatterns = [
path('dashboard/<addr>',views.dashboard_index,name='dashboard-view')
]