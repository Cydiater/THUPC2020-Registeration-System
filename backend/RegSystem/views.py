from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Users.jwtauth import *

import Users.views
import Post.views

import json


def user_auth(fn):
    def wrapped_func(request, *args, **kwargs):
        if verify(request.META.get("HTTP_AUTHORIZATION").split()[1]) == False:
            return HttpResponse(status=401)
        return fn(request, *args, **kwargs)
    return wrapped_func
def admin_auth(fn):
    def wrapped_func(request, *args, **kwargs):
        if verify_admin(
                request.META.get("HTTP_AUTHORIZATION").split()[1]) == False:
            return HttpResponse(status=401)
        return fn(request, *args, **kwargs)
    return wrapped_func
def admin_post_auth(fn):
    def wrapped_func(request, *args, **kwargs):
        if request.method == 'POST' and verify_admin(
                request.META.get("HTTP_AUTHORIZATION").split()[1]) == False:
            return HttpResponse(status=401)
        return fn(request, *args, **kwargs)
    return wrapped_func

def get_username(request):
    try:
        return get_username_jwt(
            request.META.get("HTTP_AUTHORIZATION").split()[1])
    except:
        return 'unkown error'


@user_auth
def hello(request):
    return HttpResponse("Hello world !")

@csrf_exempt
def login(request):
    data = request.body.decode('utf-8')
    signIn_info = json.loads(data)
    ret = Users.views.signIn(**signIn_info)
    return HttpResponse(json.dumps(ret, ensure_ascii=False))

@csrf_exempt
def register(request):
    data = request.body.decode('utf-8')
    registerIn_info = json.loads(data)
    ret = Users.views.registerIn(**registerIn_info)
    return HttpResponse(json.dumps(ret, ensure_ascii=False))


@csrf_exempt
@user_auth
def userinfo(request):
    if request.method == 'GET':
        teamname = request.GET.get('name')
        if teamname == None:
            return HttpResponse(status=404)
        ret = Users.views.getUserinfo(teamname)
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

    elif request.method == 'POST':
        teamname = get_username(request)
        data = request.body.decode('utf-8')
        data = json.loads(data)
        if 'members' not in data:
            return HttpResponse(status=400)
        ret = Users.views.modifyMemberinfo(teamname, data['members'])
        return HttpResponse(json.dumps(ret, ensure_ascii=False))


def checkExistence(request):
    teamname = request.GET.get('teamname')
    if teamname == None:
        return HttpResponse(status=404)
    ret = Users.views.checkExistence(teamname)
    return HttpResponse(json.dumps(ret, ensure_ascii=False))


@csrf_exempt
@admin_post_auth
def postboard(request):
    if request.method == 'GET':
        ret = Post.views.getPostboard()
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        registerIn_info = json.loads(data)

        ret = Post.views.postPostboard(**registerIn_info) if 'id' in registerIn_info \
            else Post.views.postPostboard(**registerIn_info, id = None)
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

@csrf_exempt
@user_auth
def email(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        ret = Users.views.getEmailVerifyStatus(email)
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
    elif request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        ret = Users.views.dealEmailVerifyCode(**data)
        return HttpResponse(json.dumps(ret, ensure_ascii=False))