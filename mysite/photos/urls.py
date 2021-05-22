from django.urls import path
from . import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',views.success),
    path('success/',views.success),
    path('upload',views.upload_record),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)     #url patterns to store and display files.
