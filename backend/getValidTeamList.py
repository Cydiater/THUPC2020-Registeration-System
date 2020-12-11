import json
import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RegSystem.settings")
import django
django.setup()

from Users.models import *

with open('validTeamList.csv','w') as f:
    headers = ['队伍名称', '队伍类型', 'OJ用户名']
    rows = []
    for usr in user.objects.all():
        isvalid = True
        for link in user2member.objects.filter(userid = usr.id):
            memb = member.objects.get(id = link.memberid)
            try:
                email = Email.objects.get(email=memb.email)
            except:
                isvalid = False
                print('bad' , memb.email)
            else:
                if email.emailVerifyState != 'verified':
                    isvalid = False
        account = OJaccount.objects.get(id = usr.id)
            
        if isvalid:
            print('ok')
            rows.append({
                '队伍名称' : usr.teamname, 
                '队伍类型' : usr.type.upper(), 
                'OJ用户名' : account.account,
            })

    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)