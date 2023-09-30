from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
# MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    path('portal/', views.portal, name = 'portal'),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name = 'signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]