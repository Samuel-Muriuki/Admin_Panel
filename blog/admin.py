from django.contrib import admin
from .models import Post, Todo


class PostAdminSite(admin.AdminSite):
    site_header = "KEMRI Admin"
    site_title = "KEMRI Admin Portal"
    index_title = "Welcome to KEMRI Researcher Portal"


post_admin_site = PostAdminSite(name='post_admin')


post_admin_site.register(Post)
admin.site.register(Todo)