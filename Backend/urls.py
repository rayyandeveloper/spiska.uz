from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import change

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),    
    path('api/', include('api.urls')),
    path('', include('home.urls')),
    path('support/', change)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)