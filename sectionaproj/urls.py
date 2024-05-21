from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.index_gender),
    path('users', views.index_user)
]
