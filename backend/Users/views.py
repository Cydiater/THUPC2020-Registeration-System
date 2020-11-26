from django.shortcuts import render
from django.core.mail import send_mail
from Users.models import *
from .jwtauth import generate
from random import randint

from RegSystem import settings

# Create your views here.


def signIn(username, password):
    res = {}
    try:
        usr = user.objects.get(teamname=username)
        if (usr.password == password):
            res['token'] = generate(username)
        else:
            res['message'] = '密码错误'
    except:
        res['message'] = '用户不存在'

    return res


def registerIn(teamname, password, type, members):
    res = {}
    try:
        usr = user.objects.get(teamname=teamname)
        res['status'] = 'failed'
        res['message'] = '用户名已被注册'
    except:
        try:
            if len(teamname) < 3 or len(teamname) > 20:
                raise Exception('用户名长度应大于等于3且小于等于20')
            if type not in {'a', 'b', 'c'}:
                raise Exception('unexpected error : usertype')
            for memb in members:
                if len(memb['name']) > 10:
                    raise Exception('姓名太长')
                if len(memb['school']) > 20:
                    raise Exception('学校名太长')

        except Exception as e:
            res['status'] = 'failed'
            res['message'] = str(e)
        except:
            res['status'] = 'failed'
            res['message'] = 'unknown error : register'

        else:
            userId = user.objects.create(teamname=teamname,
                                         password=password,
                                         type=type).id
            for memb in members:
                memberId = member.objects.create(**memb).id
                user2member.objects.create(userid=userId, memberid=memberId)

            res['status'] = 'success'
            res['message'] = 'register succeeded'
    return res


def getUserinfo(teamname):
    res = {}
    try:
        usr = user.objects.get(teamname=teamname)
    except:
        res['message'] = '用户名不存在'
    else:
        res['teamname'] = usr.teamname
        res['type'] = usr.type
        res['isAdmin'] = usr.isAdmin
        res['members'] = []

        for edge in user2member.objects.filter(userid=usr.id):
            try:
                memb = member.objects.get(id=edge.memberid)
            except:
                pass
            else:
                res['members'].append({
                    'name': memb.name,
                    'school': memb.school,
                    'gender': memb.gender,
                    'email': memb.email,
                    'phone': memb.phone,
                    'location': memb.location
                })
    
    while len(res['members'])<3 :
        res['members'].append({})

    return res


def checkExistence(teamname):
    res = {}
    try:
        user.objects.get(teamname=teamname)
    except:
        res['status'] = 'ok'
        res['message'] = '用户名未注册'
    else:
        res['status'] = 'error'
        res['message'] = '用户名已存在'
    return res


def modifyMemberinfo(teamname, members):
    res = {}

    try:
        userId = user.objects.get(teamname=teamname).id

        for edge in user2member.objects.filter(userid=userId):
            try:
                memb = member.objects.get(id=edge.memberid)
            except:
                res['debug'] = 'aru'
            else:
                memb.delete()
                edge.delete()

        for memb in members:
            memberId = member.objects.create(**memb).id
            user2member.objects.create(userid=userId, memberid=memberId)

        res['status'] = 'success'
        res['message'] = 'modify successed'
    except:
        res['status'] = 'failed'
        res['message'] = 'modify error'
    return res

def getEmailVerifyStatus(email):
    try:
        memb = member.objects.get(email = email)
    except:
        return {'message' : '邮箱不存在'}
    else:
        return {'status' : memb.emailVerifyState}

def dealEmailVerifyCode(action, email, code = None):
    try:
        memb = member.objects.get(email = email)
    except:
        return {'message' : '邮箱不存在'}

    if action == 'send':
        memb.emailVerifyCode = str(randint(0,999999)).zfill(6)
        memb.emailVerifyState = 'waiting'
        memb.save()

        message = '您的验证码是: ' + memb.emailVerifyCode
        send_mail(
            'THUPC邮箱验证码', 
            message = message,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        )

        return {'message' : '发送成功'}
    elif action == 'verify':
        if code == memb.emailVerifyCode:
            memb.emailVerifyState = 'verified'
            memb.save()
            return {'message' : '验证成功'}
        else:
            return {'message' : '验证失败'}
    else:
        return {'message' : 'unknow error'}