import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RegSystem.settings")
import django
django.setup()

from Users.models import OJaccount

OJaccount.objects.all().delete()

with open("./name2password.json",'r') as load_f:
    lst = json.load(load_f)
    for account in lst:
        print(account[0],account[1])
        OJaccount.objects.create(account=account[0],password=account[1])

