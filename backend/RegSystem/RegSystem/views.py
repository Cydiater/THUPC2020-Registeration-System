from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import Users.views
 
def hello(request):
    return HttpResponse("Hello world !")

@csrf_exempt
def login(request):
    data = request.body.decode('utf-8')
    signIn_info = json.loads(data)
    ret = Users.views.signIn(**signIn_info)

    return HttpResponse( json.dumps(ret, ensure_ascii=False) )