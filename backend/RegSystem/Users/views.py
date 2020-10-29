from django.shortcuts import render
from Users.models import user, member, user2member

from .jwtauth import generate

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


def registerIn(teamname, password,email,type,members):
    res = {}
    try:
        usr = user.objects.get(name=teamname)
        res['status'] = 'failed'
        res['message'] = '用户名已被注册'
    except:
        try:
            if len(teamname)<3 or len(teamname)>20:
                raise Exception('用户名长度应大于等于3且小于等于20')
            if len(password)<6 or len(password)>16:
                raise Exception('密码长度应大于等于6且小于等于16')
            if type not in {'a','b','c'}:
                raise Exception('unexpected error : usertype')
            for memb in members:
                if len(memb['name']) > 10 : 
                    raise Exception('姓名太长')
                if len(memb['school']) > 20 : 
                    raise Exception('学校名太长')
            
        except Exception as e:
            res['status'] = 'failed'
            res['message'] = str(e)
        except:
            res['status'] = 'failed'
            res['message'] = 'unknown error : register'
        else:
            userId = user.objects.create(teamname=teamname, password=password, email=email, type=type).id
            for memb in members:
                memberId = member.objects.create(name = memb['name'], school = memb['school'] ,gender = memb['gender'] ).id
                user2member.objects.create(userid = userId, memberid = memberId)

            res['status'] = 'success'
            res['message'] = 'register succeeded'
    return res
