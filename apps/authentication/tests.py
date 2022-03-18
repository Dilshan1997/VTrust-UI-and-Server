
from django.test import TestCase
from django.contrib.auth import authenticate, login,logout,password_validation
from .auth_contract import *

class AuthenticationTestCase(TestCase):
    user =authenticate(username="dila", password="ddddd")
    execTxn("loginUser",address,"username", "password")
