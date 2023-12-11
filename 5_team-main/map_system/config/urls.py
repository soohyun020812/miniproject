
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin", admin.site.urls),
    path("service/", include("service.urls")),
    path('board/', include('board.urls')),
    path('login/', include('login.urls')),
]
