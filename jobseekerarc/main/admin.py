from django.contrib import admin
from .models import Job\
    # , JobApplication


class JobAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description')
    # prepopulated_fields = {"slug": ("author", "title")}


# class JobApplicationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'job', 'resume')


admin.site.register(Job, JobAdmin)
# admin.site.register(JobApplication, JobApplicationAdmin)
