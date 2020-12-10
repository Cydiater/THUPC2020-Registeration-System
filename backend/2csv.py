import logging
import json
import os
import csv

logging.basicConfig(level=logging.DEBUG)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RegSystem.settings")
import django
django.setup()

from Users.models import user, member, Email, user2member

if __name__ == '__main__':
    headers = ['队伍名称', '队伍类型',
               '队员 1 - 姓名', '队员 1 - 学校', '队员 1 - 性别', '队员 1 - 邮箱', '队员 1 - 邮箱状态', '队员 1 - 手机号', '队员 1 - 地址',
               '队员 2 - 姓名', '队员 2 - 学校', '队员 2 - 性别', '队员 2 - 邮箱', '队员 2 - 邮箱状态', '队员 2 - 手机号', '队员 2 - 地址',
               '队员 3 - 姓名', '队员 3 - 学校', '队员 3 - 性别', '队员 3 - 邮箱', '队员 3 - 邮箱状态', '队员 3 - 手机号', '队员 3 - 地址',
               ]
    with open('signup.csv', 'w') as f:
        rows = []
        for team in user.objects.all():
            row = {}
            row['队伍名称'] = team.teamname
            row['队伍类型'] = team.type
            cnt = 1
            for link in user2member.objects.filter(userid=team.id):
                teamMember = member.objects.get(pk=link.memberid)
                row['队员 {} - 姓名'.format(cnt)] = teamMember.name
                row['队员 {} - 学校'.format(cnt)] = teamMember.school
                row['队员 {} - 邮箱'.format(cnt)] = teamMember.email
                row['队员 {} - 地址'.format(cnt)] = teamMember.location
                row['队员 {} - 手机号'.format(cnt)] = teamMember.phone
                row['队员 {} - 性别'.format(cnt)] = teamMember.gender
                if Email.objects.filter(email=teamMember.email).count() > 0:
                    row['队员 {} - 邮箱状态'.format(cnt)] = Email.objects.get(email=teamMember.email).emailVerifyState
                else:
                    row['队员 {} - 邮箱状态'.format(cnt)] = 'null'
                cnt += 1
            if cnt == 4:
                rows.append(row)
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


