from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('home', views.index, name='home'),
    path('',views.index_view,name="landing_page"),
    path('home/proposal-chart/<b_id>', views.proposalChart, name='proposal-chart'),
    path('followers', views.following_ballot_tab, name='follower_tab'),
   
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    

]
