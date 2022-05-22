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
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news', views.news),
    path('articles', views.articles),
    path('help', views.help),
    path('about', views.about),
    path('', views.main, name='home'),
    path('news/<int:pk>', views.NewsDatailView.as_view(), name='NewsDatail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include('registration.urls')),
    path('password-reset/', include('registration.urls'), name='password_reset'),
    path('password-reset/done/', include('registration.urls'), name='password_reset_done'),
    path('password-reset/confirm/(P<uidb64>[-\w])/(P<token>[-\w])/', include('registration.urls'),
         name='password_reset_confirm'),
    path('password-reset/complete/', include('registration.urls'), name='password_reset_complete'),
]
