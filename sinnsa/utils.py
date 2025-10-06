# sinnsa/utils.py
import random


def omikuji(seed_number):
    fortunes = [
        "大吉 🐉 今日は最高の運勢！",
        "中吉 🌈 チャンスはしっかり掴んで！",
        "小吉 ☕ 少しずつ前進しよう",
        "吉 ✨ 普通が一番幸せかも",
        "末吉 💫 焦らず、地道にね",
        "凶 😖 注意深く行動しよう",
        "大凶 💥 今日は静かに過ごすと吉",
    ]

    colors = [
        "赤",
        "青",
        "緑",
        "黄色",
        "紫",
        "白",
        "黒",
        "オレンジ",
        "ピンク",
        "水色",
        "茶色",
        "グレー",
        "金",
        "銀",
    ]

    advices = [
        "いつもより5分早く行動してみよう。",
        "小さなことにも「ありがとう」を言ってみて。",
        "目を閉じて深呼吸、気持ちが整うよ。",
        "失敗しても、それは次のチャンスの準備だよ。",
        "今日は「やってみよう」がキーワード！",
        "他人と比べず、自分のペースでOK。",
        "迷ったら、好きなほうを選んで正解。",
    ]

    random.seed(seed_number)

    return {
        "result": random.choice(fortunes),
        "lucky_number": random.randint(1, 9),
        "lucky_color": random.choice(colors),
        "advice": random.choice(advices),
    }
