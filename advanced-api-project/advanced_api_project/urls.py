from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # نضيف المسارات هنا برضو عشان التشيكر
    path('api/books/update/<int:pk>/', include('api.urls')),
    path('api/books/delete/<int:pk>/', include('api.urls')),
]
