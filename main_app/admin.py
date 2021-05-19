from django.contrib import admin
# import your models here
from .models import Guitar, SetUp, Wood

# Register your models here.
admin.site.register(Guitar)
admin.site.register(SetUp)
admin.site.register(Wood)