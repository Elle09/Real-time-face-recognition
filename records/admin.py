# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from records.models import Records
from .models import Records
admin.site.register(Records)
