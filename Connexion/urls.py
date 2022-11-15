from django.contrib import auth
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PageAuthentification, name='PageAuthentification'),
    path('deconnecter/', views.Deconnecter, name='Deconnexion'),
    path('profile/', views.Profile, name='profile'),
    path('admin_Connexion/', views.Connexion_Admin, name='Connexion_Admin'),
    path('PageAdmin/', views.PageAdmin, name='pageAdministrateur'),
    path('Deconnexion_admin/', views.Deconnexion_admin, name='deconnexionAdmin'),

    path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='connexion/change_password.html',
            success_url='/'
        ),
        name='change-password'
    ),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='connexion/registration/password_reset_form.html'),
         name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='connexion/registration/password_reset_done.html',
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='connexion/registration/password_reset_confirm.html',
    ), name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='connexion/registration/password_reset_complete.html'),
         name='password_reset_complete'),
]

