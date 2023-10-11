from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordResetForm,MySetPasswordForm
# MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    # path('',views.home.as_view(),name='home'),
    
    path('portal/', views.portal, name = 'portal'),

    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),

    # added to resolve unexpected redirect to this path after login 
    path('accounts/profile/', views.home,name='home'),

    path('signup/',views.SignupView.as_view(),name='signup'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('transaction/', views.TransactionView.as_view(), name='transaction'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)