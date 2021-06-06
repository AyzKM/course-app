from django.contrib import admin
from .models import Course, Branch, Contact, Category

admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Category)