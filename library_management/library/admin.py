from django.contrib import admin
from .models import Book,Stundet
# Register your models here.
@admin.register(Book)
class BoodAdmin(admin.ModelAdmin):
    list_display = ['name','author','isbn','category']

@admin.register(Stundet)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','classroom','branch','roll_no','phone']