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
import datetime
from django.core.mail import send_mail

@login_required(login_url="login/")
def indexBallot(request):
    ballot_details = BallotDetails     
    print(ballot_details)
    return render(request,"Ballot/create_ballot.html",{'form':ballot_details,'login_val':True})

prop_data=None
method=None

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
    print(prop_data)
    ballot_details = BallotDetails(request.POST or None)
    login_val=False
    msg = None
    r_value=False
 
    # print(request.POST)
    
    print(prop_data)
    auth_data=auth_contract.auth_contract.functions.getUserData().call()
    print(auth_data)
    owner_name=auth_data[3]
    owner_address=auth_data[2]
    if request.method == "POST":

        if ballot_details.is_valid():
            
            print("Valid")
            print(ballot_details.cleaned_data.get('agrements'))
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
            ballot_id=execTxn("getBallotId")
            method=""
            if published_method=='1':
                method="public"
                if now<=start_date_epoch and now<=end_date_epoch and start_date_epoch<end_date_epoch:
                    msg="Successfully Created Ballot"
                    r_value=execTxn("createBallot",email,ballot_name,ballot_description,owner_name,owner_address,start_date_epoch,end_date_epoch,method)
                    for i in range(len(prop_data.keys())):
                        execTxn('createProposal',prop_data[f"prop{i+1}"]["pid"],prop_data[f"prop{i+1}"]["prop_name"],prop_data[f"prop{i+1}"]["prop_details"])
                    return redirect('home')
                if r_value==False:
                    msg="Plz check your data"
                    return redirect('index_ballot')
                
            else:
                method="private"
                if now<=start_date_epoch and now<=end_date_epoch and start_date_epoch<end_date_epoch:
                    msg="Successfully Created Ballot"
                    r_value=execTxn("createBallot",email,ballot_name,ballot_description,owner_name,owner_address,start_date_epoch,end_date_epoch,method)
                    print("####",ballot_id,owner_address)
                    private_ballot=execTxn("savePrivateBallotIds",owner_address,ballot_id)
                    print('###############',private_ballot)
                    for i in range(len(prop_data.keys())):
                        execTxn('createProposal',prop_data[f"prop{i+1}"]["pid"],prop_data[f"prop{i+1}"]["prop_name"],prop_data[f"prop{i+1}"]["prop_details"])     
                    return redirect('private_ballot')
               

        else:
            print("not valid")

prop_count=0
def getProposalCount(request):
    global prop_count
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
            prop_count = request.GET.get("prop_count", None)
            # print(prop_count)
            return JsonResponse({"valid":True,"state":200})
         
@login_required(login_url="login/")
def gotoBallotView(request, b_id):
    # print(f"bid {b_id}")
    proposals_d=list()
    ballot_d=list(execTxn("getBallotDetails",int(b_id)))
    n=ballot_d[9]
    for i in range(n):
        proposal_details=execTxn("getProposalDetails",f'{b_id}-{i}')
        proposals_d.append(proposal_details)
    addr=auth_contract.auth_contract.functions.getUserData().call()[2]
    # print("address",addr)
    # print(ballot_d)
    # print(proposals_d)
    
    return render(request,"Ballot/ballot_details.html",{'data':ballot_d,'p_data':proposals_d,'address':addr,'login_val':True})

@login_required(login_url="login/")
def voting(request,b_id,p_id,address):
    # print("ffffffff",b_id,p_id,address)
    msg=''
    vote=execTxn('voting',int(b_id),p_id,address)
    print(vote)
    return redirect('home')
    
############PRIVATE BALLOT###############

@login_required(login_url="login/")
def privateBallot(request):
    ballot_count=0
    ballot_data=dict()
    proposal_data=dict()
    expired=True 
    today=datetime.datetime.now().strftime('%Y-%m-%d')   
    admin_address=auth_contract.execTxn("getUserData")[2]
    print(type(admin_address))
    td=int(int(time.time()))
    ballot_ids=execTxn("getPrivateBallotIds",admin_address)
    for i in ballot_ids:
        inside_data=list()
        x=list(execTxn("getBallotDetails",i))
        start_date=datetime.datetime.fromtimestamp(x[6])
        end_date=datetime.datetime.fromtimestamp(x[7])
        date_difference=(datetime.date(end_date.year,end_date.month,end_date.day)-datetime.date(start_date.year,start_date.month,start_date.day)).days
        x.append(str(start_date.strftime('%Y-%m-%d')))
        x.append(str(end_date.strftime('%Y-%m-%d')))
        if( td>=x[6]  and  x[7]>=td ):
            x.append(f'{date_difference} Days Left')
            x.append(False)
        elif(td<x[6]):
            x.append("Not Yet Published")
            x.append(True)
            
            
        else:
            x.append("Voting time is over")
            x.append(True)
            
        
        ballot_data[i]=x
        # print(ballot_data)
        
        # dates[i]=[str(start_date.strftime('%Y-%m-%d')),str(end_date.strftime('%Y-%m-%d')),date_difference]
        ballot_count=len(ballot_ids)
        
        # date_difference=(end_date-today)
        for j in range(x[9]):
            y=execTxn("getProposalDetails",f'{i}-{j}')
            inside_data.append(y)
        proposal_data[i]=inside_data
        
        labels = []
        data = []

        print(ballot_data)
    context = {'ballot_data': ballot_data,'proposal_data':proposal_data,'n':ballot_ids,'addr':admin_address,'login_val':True}
    return render(request,"Ballot/private_ballot_page.html",context)

@login_required(login_url="login/")
def gotoPrivateBallotView(request,b_id):
    proposals_d=list()
    ballot_d=list(execTxn("getBallotDetails",int(b_id)))
    n=ballot_d[9]
    for i in range(n):
        proposal_details=execTxn("getProposalDetails",f'{b_id}-{i}')
        proposals_d.append(proposal_details)
    addr=auth_contract.auth_contract.functions.getUserData().call()[2]
    # print("address",addr)
    # print(ballot_d)
    # print(proposals_d)
    
    return render(request,"Ballot/private_ballot_details.html",{'data':ballot_d,'p_data':proposals_d,'address':addr,'login_val':True})


@login_required(login_url="login/")
def privateBalloVoting(request,b_id,p_id,address):
    # print("ffffffff",b_id,p_id,address)
    msg=''
    vote=execTxn('privateBallotVoting',int(b_id),p_id,address)
    print(vote)
    return redirect('home')

@login_required(login_url="login/")
def winningProposal(request,b_id):
    winner=execTxn("winningProposal",int(b_id))
    print(winner)
    proposal_data=execTxn("getProposalDetails",winner)
    print(proposal_data)
    if request.is_ajax and request.method == "GET":
        return JsonResponse({"valid":True,"state":200,"proposal_data":proposal_data})
    
@login_required(login_url="login/")
def followers(request,b_id,addr):
    print(b_id)
    follower=execTxn("setFollowers",int(b_id),addr)
    if request.is_ajax and request.method == "GET":
        return JsonResponse({"valid":True,"state":200})
    
        
def privateBallotDetailsAnalysisChart(b_id):
    labels = []
    data = []
    print("####",b_id)
    x=list(execTxn("getBallotDetails",int(b_id)))
    for j in range(x[9]):
            y=execTxn("getProposalDetails",f'{b_id}-{str(j)}')
            print(y)
            labels.append(y[1])
            data.append(y[3])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
def privateBallotInvitationSend(request,b_id,wallet_address):
    save_voter=execTxn("savePrivateVotersData",int(b_id),wallet_address)
    if save_voter:
        status="success"
    else:
        status="Fail"
    get_voters_data=execTxn("getPrivateVotersData",int(b_id))
    print(get_voters_data)
    print(b_id,wallet_address)
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
    if request.is_ajax and request.method == "GET":
            return JsonResponse({"valid":True,"state":200,"method":method,'status':status})