from django.contrib import admin

# Register your models here.

from .models import yazar
from .models import kitap

admin.site.register(yazar)
admin.site.register(kitap)
