from django.contrib import admin
from .models import About
from .models import Contact
from .models import Skills


# Register your models here.
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Skills)

