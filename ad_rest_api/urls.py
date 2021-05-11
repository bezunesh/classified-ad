from django.urls import path
from ad_rest_api import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:pk>', views.post_detail),
]