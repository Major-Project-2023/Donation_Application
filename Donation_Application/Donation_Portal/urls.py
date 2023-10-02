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

    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),

    path('signup/',views.SignupView.as_view(),name='signup'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('transaction/', views.TransactionView.as_view(), name='transaction'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

# added to resolve unexpected redirect to this path after login
    path('accounts/profile/', views.home,name='home'),

]