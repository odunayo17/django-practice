from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('login_sys.urls')),
    path("admin/", admin.site.urls),
]
