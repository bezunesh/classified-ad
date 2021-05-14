from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from ad_rest_api import views

urlpatterns = [
    path('', views.api_root),
    path('posts/', 
        views.PostList.as_view(), 
        name='post-list'),
    path('posts/<int:pk>/', 
        views.PostDetail.as_view(),
        name='post-detail'),
    path('posts/<int:pk>/description/', 
        views.PostDescription.as_view(),
        name='post-description'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/', 
        views.UserDetail.as_view(),
        name='user-detail'),
    path('categories/', 
        views.CategoryList.as_view(),
        name='category-list'),
    path('categories/<int:pk>/', 
        views.CategoryDetail.as_view(),
        name='category-detail'),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)