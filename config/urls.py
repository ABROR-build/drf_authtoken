from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_authtoken.urls')),
    path('', include('users.urls')),
]
