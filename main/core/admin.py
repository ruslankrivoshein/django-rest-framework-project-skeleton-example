from django.contrib import admin

from .models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ()
    search_fields = ('name', )
    exclude = ('created_at', )

    class Meta:
        model = Test


admin.AdminSite.site_header = 'My site'
admin.AdminSite.site_title = 'My site'
admin.AdminSite.index_title = 'Administration'
