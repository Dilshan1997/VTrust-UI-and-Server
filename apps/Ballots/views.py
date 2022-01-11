from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BallotDetails

@login_required(login_url="login/")
def createBallot(request):
    ballot_details = BallotDetails(request.POST or None)

    login_val=False
    msg = None
    
    if request.method == "POST":
        if ballot_details.is_valid():
            email=ballot_details.cleaned_data.get("email")
            ballot_name=ballot_details.cleaned_data.get("ballot_name")
            ballot_description=ballot_details.cleaned_data.get("ballot_deatails")
            ballot_type=ballot_details.cleaned_data.get("ballot_type")
            proposal_count=ballot_details.cleaned_data.get("proposal_count")
            published_method=ballot_details.cleaned_data.get("published_method")
            start_date=ballot_details.cleaned_data.get("start_date")
            end_date=ballot_details.cleaned_data.get("end_date")
            
            print(email,ballot_name,ballot_type,ballot_description,ballot_description,proposal_count,published_method,start_date,end_date)
            
    
    return render(request,"Ballot/create_ballot.html",{'form':ballot_details,'login_val':True})
