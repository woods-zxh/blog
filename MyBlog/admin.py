
from django.contrib import admin

from .models import superuser,diary,IMG,comment

admin.site.register(superuser)
admin.site.register(diary)

admin.site.register(IMG)

admin.site.register(comment)
