from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Users.jwtauth import *

import json
import Users.views


def user_auth(fn):
    def wrapped_func(request, *args, **kwargs):
        if verify(request.META.get("HTTP_AUTHORIZATION")) == False:
            return HttpResponse(status=401)
        return fn(request, *args, **kwargs)

    return wrapped_func


def admin_auth(fn):
    def wrapped_func(request, *args, **kwargs):
        if verify_admin(request.META.get("HTTP_AUTHORIZATION")) == False:
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


def userinfo(request):
    teamname = request.GET.get('name')
    if teamname == None:
        return HttpResponse(status=404)
    ret = Users.views.getUserinfo(teamname)
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
    print("get in ")
    if request.method == 'GET':
        ret = Users.views.getPostboard()
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        registerIn_info = json.loads(data)
        dictionary = {}
        try:
            dictionary['id'] = registerIn_info['id']
        except:
            pass
        dictionary['content'] = registerIn_info['content']
        dictionary['author'] = registerIn_info['author']
        dictionary['title'] = registerIn_info['title']
        ret = Users.views.postPostboard(dictionary)
        return HttpResponse(json.dumps(ret, ensure_ascii=False))