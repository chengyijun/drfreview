# Create your tests here.
import os
import sys

import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfreview.settings")

django.setup()
from api03.models import Dog

# for i in range(10):
#     Dog.mm.create(name=f"小黄{i}")


dogs = Dog.mm.all()
print(dogs)

gt__ = Dog.mm.get_id_gt_5()
print(gt__)
lt__ = Dog.mm.get_id_lt_5()
print(lt__)
