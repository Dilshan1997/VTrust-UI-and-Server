# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from cProfile import label
from operator import le
from tracemalloc import start
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from apps.Ballots import ballot_contract_controller
from apps.authentication import auth_contract
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time

def index_view(request):
    return render(request,'home/landingpage.html')

@login_required(login_url="login/")
def index(request):
    ballot_count=0
    ballot_data=dict()
    proposal_data=dict()
    follower_btn=True
    # dates=dict()
    n=ballot_contract_controller.execTxn("getBallotId")
    today=datetime.datetime.now().strftime('%Y-%m-%d')
    user_address=auth_contract.auth_contract.functions.getUserData().call()[2]
    print(user_address)
    print(today)
    td=int(int(time.time()))
    print(td,)
    for i in range(n):
        inside_data=list()
        x=list(ballot_contract_controller.execTxn("getBallotDetails",i))
        print("$$$$$",x)
        if(x[8]=="private"):
            continue
        start_date=datetime.datetime.fromtimestamp(x[6])
        end_date=datetime.datetime.fromtimestamp(x[7])
        date_difference=(datetime.date(end_date.year,end_date.month,end_date.day)-datetime.date(start_date.year,start_date.month,start_date.day)).days
        x.append(str(start_date.strftime('%Y-%m-%d')))
        x.append(str(end_date.strftime('%Y-%m-%d')))
        
        if( td>=x[6]  and  x[7]>=td ):
            x.append(f'{date_difference} Days Left')
            x.append(False) #voting disabled or not
            x.append(False) #winner btn disabled or not
        elif(td<x[6]):
            x.append("Not Yet Published")
            x.append(True)
            x.append(False)
           
        else:
            x.append("Voting time is over")
            x.append(True)
            x.append(True)
            
        if len(x[11])==0:
            x.append(True) #Not Following Yet
        elif str(user_address) in x[11]:
            x.append(False)
        
        print("#####",follower_btn)
        
        ballot_data[i]=x
        # print(ballot_data)
        
        # dates[i]=[str(start_date.strftime('%Y-%m-%d')),str(end_date.strftime('%Y-%m-%d')),date_difference]
        ballot_count=ballot_contract_controller.execTxn("getBallotId")
        
        # date_difference=(end_date-today)
        for j in range(x[9]):
            y=ballot_contract_controller.execTxn("getProposalDetails",f'{i}-{j}')
            inside_data.append(y)
        proposal_data[i]=inside_data
        
        labels = []
        data = []

        print(ballot_data)
    context = {'ballot_data': ballot_data,'proposal_data':proposal_data,'n':ballot_count,'addr':user_address,'login_val':True}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

        
            

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    

def proposalChart(request,b_id):
    labels = []
    data = []
    urls=[]
    # ballot_count=ballot_contract_controller.execTxn("getBallotId")
    # for i in range(ballot_count):
    #     urls.append(f"home/proposal-chart/{i}")
        
    
    x=list(ballot_contract_controller.execTxn("getBallotDetails",int(b_id)))
    for j in range(x[9]):
            y=ballot_contract_controller.execTxn("getProposalDetails",f'{b_id}-{str(j)}')
            print(y)
            labels.append(y[1])
            data.append(y[3])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
def following_ballot_tab(request):
    user_address=auth_contract.execTxn("getUserData")[2]
    following_ballots= ballot_contract_controller.execTxn("getFollowingBallots",user_address)
    print(following_ballots)
    ballot_data=dict()
    proposal_data=dict()
    today=datetime.datetime.now().strftime('%Y-%m-%d')
    user_address=auth_contract.auth_contract.functions.getUserData().call()[2]
    td=int(int(time.time()))
    if len(following_ballots)!=0:
        for i in following_ballots:
            inside_data=list()
            x=list(ballot_contract_controller.execTxn("getBallotDetails",i))
            print("$$$$$",x)
            if(x[8]=="private"):
                continue
            start_date=datetime.datetime.fromtimestamp(x[6])
            end_date=datetime.datetime.fromtimestamp(x[7])
            date_difference=(datetime.date(end_date.year,end_date.month,end_date.day)-datetime.date(start_date.year,start_date.month,start_date.day)).days
            x.append(str(start_date.strftime('%Y-%m-%d')))
            x.append(str(end_date.strftime('%Y-%m-%d')))
            
            if( td>=x[6]  and  x[7]>=td ):
                x.append(f'{date_difference} Days Left')
                x.append(False) #voting disabled or not
                x.append(False) #winner btn disabled or not
            elif(td<x[6]):
                x.append("Not Yet Published")
                x.append(True)
                x.append(False)
            
            else:
                x.append("Voting time is over")
                x.append(True)
                x.append(True)

            ballot_data[i]=x
            # print(ballot_data)
            
            # dates[i]=[str(start_date.strftime('%Y-%m-%d')),str(end_date.strftime('%Y-%m-%d')),date_difference]
            ballot_count=ballot_contract_controller.execTxn("getBallotId")
            
            # date_difference=(end_date-today)
            for j in range(x[9]):
                y=ballot_contract_controller.execTxn("getProposalDetails",f'{i}-{j}')
                inside_data.append(y)
            proposal_data[i]=inside_data
            
            labels = []
            data = []

    print(ballot_data)   
    
    return render(request,'home/following_ballots.html',{'ballot_data': ballot_data,'proposal_data':proposal_data})
    
