from django.contrib import admin

# Register your models here.
from collector.models import AuthUser, Submit

admin.site.register(AuthUser)
admin.site.register(Submit)
