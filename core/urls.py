# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    
    path("VTrust/", include("apps.authentication.urls")), # Auth routes - login / register
    path("VTrust/", include("apps.home.urls")),             # UI Kits Html files
    path("VTrust/",include("apps.Ballots.urls")), #Ballot urls
    path("VTrust/",include("apps.dashboard.urls")), #dashboard urls
]
