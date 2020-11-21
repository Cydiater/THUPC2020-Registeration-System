from django.shortcuts import render
from Post.models import *
import time

# Create your views here.

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