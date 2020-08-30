from django.contrib import admin
from .models import CV , Employment, Interest , Qualification, Skill
# Register your models here.
admin.site.register(CV)
admin.site.register(Employment)
admin.site.register(Interest)
admin.site.register(Qualification)
admin.site.register(Skill)