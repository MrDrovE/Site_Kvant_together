from django.urls import path, include

from . import views as v
from django.contrib.auth import views

urlpatterns = [
    path('register/', v.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/(P<uidb64>[-\w])/(P<token>[-\w])/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
