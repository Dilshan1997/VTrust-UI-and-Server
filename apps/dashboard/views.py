from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from apps.Ballots import ballot_contract_controller
from apps.Ballots.views import followers
from apps.authentication import auth_contract
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time
import json

def dashboard_index(request):
    user_address=auth_contract.execTxn("getUserData")[2]
    owner_belongs_ballot_ids=ballot_contract_controller.execTxn("dashboardData",user_address)
    ballot_count=len(owner_belongs_ballot_ids)
    ballot_data=dict()
    proposal_data=dict()
    expired=True
    today=datetime.datetime.now().strftime('%Y-%m-%d')
    most_voting_count_from="Not Any Data"
    full_vote_count=0
    ballot_vote_count=0
    followers_count=0
    
    if len(owner_belongs_ballot_ids)!=0:
        most_famous_ballot_id=owner_belongs_ballot_ids[0]
    td=int(int(time.time()))
    for i in owner_belongs_ballot_ids:
        inside_data=list()
        x=list(ballot_contract_controller.execTxn("getBallotDetails",i))
        ballot_vote_count=x[10]
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
        full_vote_count=full_vote_count+x[10]
        ballot_data[i]=x
        # print(ballot_data)
        if x[10]>ballot_data[most_famous_ballot_id][10]:
            most_famous_ballot_id=x[0]
        # dates[i]=[str(start_date.strftime('%Y-%m-%d')),str(end_date.strftime('%Y-%m-%d')),date_difference]
        # date_difference=(end_date-today)
        followers_count=followers_count+len(x[11])
        for j in range(x[9]):
            y=list(ballot_contract_controller.execTxn("getProposalDetails",f'{i}-{j}'))
            print(y)
            if y[3]!=0:
                percentage=int(y[3]/ballot_vote_count*100)
                y.append(percentage)
            inside_data.append(y)
        proposal_data[i]=inside_data
        labels = []
        data = []
        print(ballot_data)
    print(proposal_data)
    if len(owner_belongs_ballot_ids)!=0:
        most_voting_count_from=ballot_data[most_famous_ballot_id][2]
    context = {'ballot_data': ballot_data,'proposal_data':proposal_data,'login_val':True}
    json_data=json.dumps(context)
    return render(request,'Dashboard/main.html',{"data":json_data,'ballot_data': ballot_data,'proposal_data':proposal_data,'login_val':True,'n':ballot_count,'addr':user_address,'full_vote_count':full_vote_count,'most_voting_count_from':most_voting_count_from,'followers_count':followers_count})