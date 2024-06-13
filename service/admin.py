from django.contrib import admin
from service.models import Service1

class ServiceAdmin(admin.ModelAdmin):
    list_display=('question','answer','solution','op1','op2','op3','op4')

admin.site.register(Service1,ServiceAdmin)

# Register your models here.
from django.contrib import admin

# Register your models here.
