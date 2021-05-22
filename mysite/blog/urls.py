from django.urls import path
from . import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',views.homepage),
    path('view/',views.getimg),
    path('view/success/',views.success),
    path('view/showmed/',views.display_media),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
