
from django.urls import path, re_path
from apps.Ballots import views


urlpatterns = [

    # The ballot page
    path('ballot/create', views.indexBallot, name='index_ballot'),
    path('ballot/create/proposal_num', views.getProposalCount, name = "proposal_num"),
    path('ballot/create/proposal_data', views.getProposalData, name = "proposal_data"),
    path('home/', views.createBallot, name='create_ballot'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    

]
