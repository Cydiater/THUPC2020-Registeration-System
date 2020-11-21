from django.shortcuts import render
from Users.models import user, member, user2member, post
import time
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

    #try:
    if True:
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
    #except:
        #res['status'] = 'failed'
        #res['message'] = 'modify error'
    return res


def getPostboard():
    return_list = []
    post_list = post.objects.all()
    for p in post_list:
        dictionary = {}
        dictionary['content'] = p.content
        dictionary['author'] = p.author
        dictionary['timestamp'] = p.timestamp
        dictionary['post_id'] = p.id
        dictionary['title'] = p.title
        return_list.append(dictionary)
    return return_list


def postPostboard(id, content, author, title, timestamp):
    res={}
    if id != None:
        try:
            target_post = post.objects.get(id = id)
        except:
            res = {'status': 'error', 'msg': 'invalid id'}
        else:
            if content == None or content == '':
                target_post.delete()
                res = {'status': 'ok', 'msg': 'successfully deleted'}
            else:
                target_post.content = content
                target_post.author = author
                target_post.title = title
                target_post.timestamp = time.time()
                target_post.save()
                res = {'status': 'ok', 'msg': 'successfully edited'}
    else:
        post.objects.create(content=content,
                            author=author,
                            timestamp=time.time(),
                            title=title)

        res = {'status': 'ok', 'msg': 'successfully added'}

    return res
