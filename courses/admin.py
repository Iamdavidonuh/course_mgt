from django.contrib import admin
from courses import models

# Register your models here.


admin.site.register(models.Subject)
admin.site.register(models.Course)
admin.site.register(models.Module)
