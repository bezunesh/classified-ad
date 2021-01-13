from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm, PwdChangeForm, PwdResetForm, SetPwdForm

app_name = 'ad'

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/<int:user_id>', views.profile, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        form_class=PwdChangeForm, success_url=reverse_lazy('ad:password_change_done')), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=PwdResetForm, 
        success_url=reverse_lazy('ad:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=SetPwdForm, success_url=reverse_lazy('ad:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>', views.category, name='category'),
    path('post/<int:post_id>', views.post, name='post'),
    path('createAd/', views.createAd, name='create-ad'),
    path('user/<int:user_id>/posts/', views.userPosts, name='user_posts')
]