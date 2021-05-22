from django.urls import path
from . import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('success/',views.success),
    path('',views.upload_record),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)     #url patterns to store and display files.
