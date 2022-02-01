from django.shortcuts import render
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
# Create your views here.
def dashboard_index(request,addr):
    print(addr)
    return render(request,'Dashboard/main.html',{'login_val':True})