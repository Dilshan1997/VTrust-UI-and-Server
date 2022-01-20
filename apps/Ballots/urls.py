
from django.urls import path, re_path
from apps.Ballots import views
from apps.Ballots.views import getProposalCount,getProposalData

urlpatterns = [

    # The ballot page
    path('ballot/create', views.createBallot, name='create_ballot'),
    path('ballot/create/proposal_num', getProposalCount, name = "proposal_num"),
    path('ballot/create/proposal_data', getProposalData, name = "proposal_data")

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    

]
