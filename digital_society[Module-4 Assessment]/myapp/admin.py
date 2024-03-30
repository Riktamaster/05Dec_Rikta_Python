from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Chairman)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(NoticeView)
admin.site.register(Transaction)
admin.site.register(Visitor)
admin.site.register(Watchmen)
