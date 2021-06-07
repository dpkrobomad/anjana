# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import ServiceName,ServiceCats,Account

# Register your models here.
admin.site.register(ServiceName)
admin.site.register(ServiceCats)
admin.site.register(Account)