from django.urls import path
from rest_framework import authtoken
from rest_framework.authtoken import views

from mailing import views

urlpatterns = [
    path('create-mail-user/', views.CreateMailUser.as_view()),
    path('delete-mail-user/', views.DeleteMailUser.as_view()),
    path('change-mail-user/', views.ChangeMailUser.as_view()),
]
