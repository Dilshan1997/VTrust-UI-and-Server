from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def createBallot(request):
    
    return render(request,"Ballot/create_ballot.html",{'login_val':True})