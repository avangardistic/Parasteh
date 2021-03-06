from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path('tinymce/', include('tinymce.urls')), # tinymce 
    path("admin/", admin.site.urls),
    
    path("blog/", include("blog.urls")),
    path("", home, name="home"),
]

urlpatterns += static(settings.STATIC_URL)  # Adds static to site
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # adds media to site
