from django.contrib import admin
# import your models here
from .models import Guitar, SetUp

# Register your models here.
admin.site.register(Guitar)
admin.site.register(SetUp)