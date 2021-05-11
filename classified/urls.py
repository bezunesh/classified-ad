import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from ad import views

urlpatterns = [
   # path('', views.index, name='index'),
    path('', include('ad_rest_api.urls')),
    path('ad/', include('ad.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
