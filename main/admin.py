from django.contrib import admin

from .models import Commission, Art

@admin.register(Commission)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['name', 'pub_date', 'email', 'sub_date']
    list_filter = ('done',)
    list_display = ('name','email', 'pub_date')
    readonly_fields = [
    "art",
    "name",
    "pub_date",
    "address",
    "email",
    "phone_number",
    "size",
    "attachment",
    "details",
    ]

@admin.register(Art)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['first_name', 'last_name', 'pub_date']
    list_display = ('name', 'pub_date')

# Register your models here
admin.site.site_header = "NITYA's BITCH ASS Admin"
admin.site.site_title = "NITYA's BITCH ASS Admin Portal"
admin.site.index_title = "Welcome to NITYA's BITCH ASS admin panel"
