from django.urls import path
from newtest import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import *
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'post', views.PassIdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^test/.+$', views.upload_file),
    url(r'^test2/.+$',views.show_file),
    url(r'^api-auth/', include('rest_framework.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)