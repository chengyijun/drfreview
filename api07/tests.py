import os
import sys

import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfreview.settings")

django.setup()
from api07.models import UserInfo, Role

# u1 = UserInfo.objects.create(username="abel")
# UserToken.objects.create(token=str(uuid4()), user=u1)

# 正向查找
# ut: UserToken = UserToken.objects.first()
# print(ut.user)


# 反向查找
user: UserInfo = UserInfo.objects.first()
print(user)
# print(user.user_token.all())


roles = user.user_roles.all()
print(roles)

r1: Role = Role.objects.filter(role_name="老师").first()

print(r1.users.all())

# r1.users.add(UserInfo.objects.create(username="rox"))
