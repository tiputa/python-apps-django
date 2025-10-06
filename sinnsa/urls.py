# sinnsa/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.omikuji_form, name="omikuji"),
    path("result/", views.omikuji_result, name="omikuji_result"),
]
