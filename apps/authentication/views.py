# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from logging import log
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from web3.datastructures import T
from apps.authentication.decorator import unauthenticated_user
from .forms import LoginForm, SignUpForm
from django.contrib.auth.views import LogoutView
from web3 import Web3
import time
import sys
from .auth_contract import *
from connection import connection

@unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)
    login_val=False
    msg = None
    
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
           
            user_blockchian = execTxn("loginUser",username, password)
            # status=execTxn("checkIsUserLogged",connection.wallet_address)
            # print(status)
            login_status=execTxn("checkIsUserLogged",connection.wallet_address)
            print("login status:",login_status)
            
            print(user_blockchian)
            if user_blockchian:
                user =authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    login_val=True
                    # render(request,"home/index.html",{'login_val':login_val})
                    return redirect('home')
            else:
                
                msg = 'Invalid credentials'
        else:
            
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

@unauthenticated_user
def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            blockchain_user_store = execTxn("registerUser",username, email,raw_password)
          
            if blockchain_user_store==True:
                form.save()
                msg = 'User created - please <a href="/login">login</a>.'
                success = True
            else:
                msg='Blockchain Error'
                

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def logout_view(request):
    logout_blockchain=execTxn("logoutUser")
    # print(logout_blockchain)
    logout_status=execTxn("checkIsUserLogged",connection.wallet_address) #logout_status 
    if logout_status==False:
            logout(request)

    print(logout_status)
    
    return render(request, 'home/landingpage.html')
    
    



