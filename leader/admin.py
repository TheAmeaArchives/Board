from django.contrib import admin
from .models import Curation, Post
# Register your models here.

class CurationAdmin(admin.ModelAdmin):
    list_display = ("user","text", "accepted", "created_at", "updated",)
    list_filter= ("created_at", "accepted",)

class PostAdmin(admin.ModelAdmin):
    list_display =("user",'title',"points",)



#The admin sections would be registered here
admin.site.register(Curation, CurationAdmin)
admin.site.register(Post, PostAdmin)


