from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse

admin.site.site_header = "Achivers Academy Admins"
admin.site.site_title = "Achivers Admin Portal"
admin.site.index_title = "Welcome to Achivers Academy Admin"

#
def custom_admin_view(request):
    context = dict(
        admin.site.each_context(request),
        title="Achivers Admin Page",
    )
    return TemplateResponse(request, "admin/custom_admin_view.html", context)

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom-admin-view/', self.admin_view(custom_admin_view))
        ]
        return custom_urls + urls

admin_site = CustomAdminSite(name='custom_admin')
