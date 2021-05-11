from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ad_rest_api import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:pk>', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)