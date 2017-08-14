from django.contrib import admin

# Register your models here.

from Blog.models import *
##自定制admin登陆，就是用auth_admin.UserProfileAdmin这里定义的登陆方式登陆
admin.site.register(Catagory)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
