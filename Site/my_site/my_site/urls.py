"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from app import views
from django.contrib.auth import views as views2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news', views.news),
    path('articles', views.articles),
    path('help', views.help),
    path('about', views.about),
    path('', views.main, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('password-reset/', views2.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views2.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/(P<uidb64>[-\w])/(P<token>[-\w])/', views2.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', views2.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
