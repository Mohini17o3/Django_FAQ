from django.contrib import admin
from .models import FAQ
from .models import TranslatedFAQ


# Register your models here.

admin.site.register(FAQ)
admin.site.register(TranslatedFAQ)
    