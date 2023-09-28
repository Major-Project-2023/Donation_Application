from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portal/', views.portal, name = 'portal'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name = 'signup'),
]