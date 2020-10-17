from django.shortcuts import render
from Users.models import user

from .jwtauth import generate

# Create your views here.


def signIn(username, password):
    res = {}

    try:
        print("caonima")
        usr = user.objects.get(name=username)
        print(usr.password)
        if (usr.password == password):
            res['token'] = generate(username)
        else:
            res['message'] = 'wrong password'
    except:
        res['message'] = 'no such user'

    return res


def registerIn(username, password):
    res = {}
    try:
        usr = user.objects.get(name=username)
        res['status'] = 0
        res['message'] = 'username already existed'
    except:
        user.objects.create(name=username, password=password)
        res['status'] = 1
        res['message'] = 'register succeeded'
    return res
