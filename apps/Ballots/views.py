from os import system
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import BallotDetails
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .ballot_contract_controller import *
import sys
from connection import connection
from apps.authentication import auth_contract

print(auth_contract.auth_contract.functions.getUserData().call())
@login_required(login_url="login/")
def indexBallot(request):
    ballot_details = BallotDetails     
    print(ballot_details)
    return render(request,"Ballot/create_ballot.html",{'form':ballot_details,'login_val':True})



@login_required(login_url="login/")
def createBallot(request):
    ballot_details = BallotDetails(request.POST or None)
    login_val=False
    msg = None
    
    if request.method == "POST":
        if ballot_details.is_valid():
            print("Valid")
            email=ballot_details.cleaned_data.get("email")
            ballot_name=ballot_details.cleaned_data.get("ballot_name")
            ballot_description=ballot_details.cleaned_data.get("ballot_details")
            proposal_count=ballot_details.cleaned_data.get("proposal_count")
            published_method=ballot_details.cleaned_data.get("published_method")
            start_date=ballot_details.cleaned_data.get("start_date")
            end_date=ballot_details.cleaned_data.get("end_date")
            ballot_data={"email":email,"b_name":ballot_name,"b_des":ballot_description,"prop_count":proposal_count,"pub_method":published_method,"start_date":start_date,"end_date":end_date}
            print(ballot_data)
     
            return render(request,"home/index.html",{'data':ballot_data,'login_val':True})
            
            
        else:
            print("not valid")


prop_count=0
def getProposalCount(request):
    global prop_count
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
            prop_count = request.GET.get("prop_count", None)
            print(prop_count)
            return JsonResponse({"valid":True,"state":200})
         
@csrf_exempt
def getProposalData(request):
    if request.is_ajax and request.method == "POST":
            prop_data = json.loads(request.POST.get("prop_data", None))
            print(prop_data)
            return JsonResponse({"valid":True,"state":200})