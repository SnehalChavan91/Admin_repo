from django.contrib import admin

# Register your models here.
class BookstoreAdminArea(admin.AdminSite):
    site_header="Book Store Admin Area"

bookstore_site=BookstoreAdminArea(name="BookstoreAdmin")