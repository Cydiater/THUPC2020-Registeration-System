from django.shortcuts import render
from Users.models import user

# Create your views here.

def signIn(username, password):
    res = {}

    try:
        usr = user.objects.get(name = username)
        if(usr.password == password):
            res['token'] = 'authenticated'
        else:
            res['message'] = 'wrong password'
    except :
        res['message'] = 'no such user'
        
    return res