from django.contrib import admin

# Register your models here.


#自动注册算法 如下代码

from myapp.models import *
import inspect,sys

clsmemebers = inspect.getmembers(sys.modules[__name__],inspect.isclass)
for name,cls in clsmemebers:
    admin.site.register(cls)