from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Users.jwtauth import verify

import json
import Users.views


def user_auth(fn):
    def wrapped_func(request, *args, **kwargs):
        if verify(request.META.get("HTTP_AUTHORIZATION")) == False:
            return HttpResponse("401")
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
    if teamname == None :
        return HttpResponse("404")
    ret = Users.views.getUserinfo(teamname)
    return HttpResponse(json.dumps(ret, ensure_ascii=False))

def checkExistence(request):
    teamname = request.GET.get('teamname')
    if teamname == None :
        return HttpResponse("404")
    ret = Users.views.checkExistence(teamname)
    return HttpResponse(json.dumps(ret, ensure_ascii=False))