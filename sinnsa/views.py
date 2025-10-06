# sinnsa/views.py
from django.shortcuts import render
from .utils import omikuji


def omikuji_form(request):
    """入力フォームページ"""
    return render(request, "sinnsa/index.html")


def omikuji_result(request):
    """結果ページ"""
    context = {}
    try:
        user_input = int(request.GET.get("number"))
        if 1 <= user_input <= 99:
            context["fortune"] = omikuji(user_input)
        else:
            context["error"] = "⚠️ 1〜99の数字を入力してね。"
    except (ValueError, TypeError):
        context["error"] = "⚠️ 数字をちゃんと入力してね。"

    return render(request, "sinnsa/result.html", context)
