from django.contrib import admin
from . import models


class BlogAdminArea(admin.AdminSite):
    site_header="Blog Admin Area"


blog_site=BlogAdminArea(name="Blog Admin")

admin.site.register(models.Post)
blog_site.register(models.Post)