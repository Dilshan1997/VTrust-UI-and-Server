
from django.urls import path, re_path
from apps.Ballots import views

urlpatterns = [

    # The ballot page
    path('ballot/create', views.createBallot, name='create_ballot'),
    

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    

]
