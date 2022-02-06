
from django.urls import path, re_path
from apps.Ballots import views


urlpatterns = [
    # The ballot page
    path('ballot/create', views.indexBallot, name='index_ballot'),
    path('ballot/create/proposal_num', views.getProposalCount, name = "proposal_num"),
    path('ballot/create/proposal_data', views.getProposalData, name = "proposal_data"),
    path('home/', views.createBallot, name='create_ballot'),
    path('ballot/<b_id>',views.gotoBallotView,name="BallotView"),
    path('ballot/<b_id>/<p_id>/<address>/vote',views.voting,name="Voting"),
    path('ballot/private/',views.privateBallot,name="private_ballot"),
    path('ballot/private/<b_id>',views.gotoPrivateBallotView,name="PrivateBallotView"),
    path('ballot/private/<b_id>/<p_id>/<address>/vote',views.privateBalloVoting,name="PrivateVoting")

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    
]
