import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views

from quickstart import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include(router.urls)),
    path('ad/', include('ad.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
