
from django.contrib import admin
from .models import Job, Category, Apply

# # Register your models here.
# # admin.site.register(Job) ---> this is the basic way of model registration

# # customize my models here..
class JobAdmin(admin.ModelAdmin):
    # list_display =[]
    # list_filter = []
    list_display = ['title', 'job_type', 'vacancy', 'salary', 'experience', 'category']
    list_filter = ['job_type', 'experience', 'salary']
    search_fields = ['job_type', 'salary']
 


class CategoryAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['name']

class ApplyAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['name', 'email', 'website', 'cv', 'created_at']

admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Apply, ApplyAdmin)

# admin.site.register(Job)
# admin.site.register(Category)
# admin.site.register(Apply)