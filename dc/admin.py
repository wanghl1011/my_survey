from django.contrib import admin

# Register your models here.
from dc.models import *
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
