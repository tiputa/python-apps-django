from django.shortcuts import render
import random


def index(request):
    return render(request, "work07/index.html")


# おみくじ
def omikuji(request):
    results = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
    result = random.choice(results)
    return render(request, "work07/omikuji.html", {"result": result})


# じゃんけん
def janken(request):
    hands = ["グー", "チョキ", "パー"]
    result = None
    user_hand = None
    if request.method == "POST":
        user_hand = request.POST.get("hand")
        cpu_hand = random.choice(hands)

        # 勝敗判定
        if user_hand == cpu_hand:
            result = "あいこ"
        elif (
            (user_hand == "グー" and cpu_hand == "チョキ")
            or (user_hand == "チョキ" and cpu_hand == "パー")
            or (user_hand == "パー" and cpu_hand == "グー")
        ):
            result = "あなたの勝ち！"
        else:
            result = "あなたの負け…"

        return render(
            request,
            "janken.html",
            {"user": user_hand, "cpu": cpu_hand, "result": result},
        )

    return render(request, "work07/janken.html", {"result": result})


# Hi & Low
def hilow(request):
    player_card = random.randint(1, 13)
    cpu_card = None
    result = None
    if request.method == "POST":
        choice = request.POST.get("choice")  # High or Low
        player_card = int(request.POST.get("player_card"))
        cpu_card = random.randint(1, 13)

        if (choice == "High" and cpu_card > player_card) or (
            choice == "Low" and cpu_card < player_card
        ):
            result = "あなたの勝ち！"
        elif cpu_card == player_card:
            result = "引き分け"
        else:
            result = "あなたの負け…"

    return render(
        request,
        "work07/hilow.html",
        {"player_card": player_card, "cpu_card": cpu_card, "result": result},
    )
