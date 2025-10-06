from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # トップページ
    path("reiwa/", views.reiwa, name="reiwa"),  # 令和→西暦変換
    path("bmi/", views.bmi, name="bmi"),  # BMI計算
    path("warikan/", views.warikan, name="warikan"),  # 割り勘
    path("chokin/", views.chokin, name="chokin"),  # 貯金
    path("calculator/", views.calculator, name="calculator"),  # 四則演算
]
