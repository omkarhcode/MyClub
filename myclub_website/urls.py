from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
]

# Configure Admin titles
admin.site.site_header = "My Club Administration"
admin.site.site_title = "Admin"
admin.site.index_title = "Welcome to Admin "
