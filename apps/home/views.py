# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from apps.Ballots import ballot_contract_controller


def index_view(request):
    return render(request,'home/landingpage.html')

@login_required(login_url="login/")
def index(request):
    ballot_data=dict()
    proposal_data=dict()
    
    n=ballot_contract_controller.execTxn("getBallotId")
    print(n)
    for i in range(n):
        inside_data=list()
        x=list(ballot_contract_controller.execTxn("getBallotDetails",i))
        ballot_data[i]=x
        for j in range(x[9]):
            y=ballot_contract_controller.execTxn("getProposalDetails",f'{i}-{j}')
            inside_data.append(y)
        proposal_data[i]=inside_data
        
            
    print(ballot_data)
    print(proposal_data)
    context = {'ballot_data': ballot_data,'proposal_data':proposal_data,'login_val':True}

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
