import os
import sys

import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfreview.settings")

django.setup()

# 导入模块必须在 上面的django环境启动之后 要不然会报错
from api02.models import UserInfo, Role

# UserInfo.objects.create(user_name="子龙")
# UserInfo.objects.create(user_name="云长")
# UserInfo.objects.create(user_name="翼德")
#
# Role.objects.create(role_name="演员")
# Role.objects.create(role_name="导演")
#
ui1: UserInfo = UserInfo.objects.filter(id=1).first()
ui2: UserInfo = UserInfo.objects.filter(id=2).first()
ui3: UserInfo = UserInfo.objects.filter(id=3).first()
role1: Role = Role.objects.filter(id=1).first()
# role2: Role = Role.objects.filter(id=2).first()
# # role1.users.add(ui1)
# # role1.users.add(ui2)
# role2.users.add(ui1)
# role2.users.add(ui3)


res = ui1.roles.all()
print(res)

res2 = role1.users.all()
print(res2)
