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
import time


@login_required(login_url="login/")
def indexBallot(request):
    ballot_details = BallotDetails     
    print(ballot_details)
    return render(request,"Ballot/create_ballot.html",{'form':ballot_details,'login_val':True})

prop_data=None

@csrf_exempt
def getProposalData(request):
    global prop_data
    if request.is_ajax and request.method == "POST":
        prop_data = json.loads(request.POST.get("prop_data", None))
        # print(prop_data)
        return JsonResponse({"valid":True,"state":200})
        
@login_required(login_url="login/")
def createBallot(request):
    global prop_data
    ballot_details = BallotDetails(request.POST or None)
    login_val=False
    msg = None
    # print(request.POST)
    
    print(prop_data)
    auth_data=auth_contract.auth_contract.functions.getUserData().call()
    print(auth_data)
    owner_name=auth_data[3]
    owner_address=auth_data[2]
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
            print(published_method)
            p='%Y-%m-%d'
            print(start_date,end_date)
            now=time.time()
            print(int(now))
            start_date_epoch = int(time.mktime(time.strptime(str(start_date),p)))
            end_date_epoch=int(time.mktime(time.strptime(str(end_date),p)))
            print(start_date_epoch,end_date_epoch)
            ballot_data={"email":email,"b_name":ballot_name,"b_des":ballot_description,"prop_count":proposal_count,"pub_method":published_method,"start_date":start_date,"end_date":end_date}
            # print(ballot_data)
            method=""
            if published_method=='1':
                method="public"
            else:
                method="private"
            print(method)
            if now<=start_date_epoch and now<=end_date_epoch and start_date_epoch<end_date_epoch:
                msg="Successfully Created Ballot"
                r_value=execTxn("createBallot",email,ballot_name,ballot_description,owner_name,owner_address,start_date_epoch,end_date_epoch,method)
            
                for i in range(len(prop_data.keys())):
                    execTxn('createProposal',prop_data[f"prop{i+1}"]["pid"],prop_data[f"prop{i+1}"]["prop_name"],prop_data[f"prop{i+1}"]["prop_details"])
                
                if r_value:
                    
                    return redirect('home')
            else:
                return redirect('index_ballot')
            
            
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
         

def gotoBallotView(request, b_id):
    print(f"bid {b_id}")
    ballot_d=list(execTxn("getBallotDetails",int(b_id)))
    print(ballot_d)
    return render(request,"Ballot/ballot_details.html",{'data':ballot_d,'login_val':True})