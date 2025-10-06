from django.shortcuts import render


def index(request):
    return render(request, "work06/index.html")


def reiwa(request):
    result = None
    if request.method == "POST":
        try:
            reiwa_year = int(request.POST.get("reiwa_year"))
            seireki = 2018 + reiwa_year  # 令和元年 = 2019年
            result = f"令和{reiwa_year}年 は 西暦 {seireki}年 です"
        except Exception:
            result = "入力エラー"
    return render(request, "work06/reiwa.html", {"result": result})


def bmi(request):
    result = None
    if request.method == "POST":
        try:
            height = float(request.POST.get("height"))
            weight = float(request.POST.get("weight"))
            bmi_value = round(weight / ((height / 100) ** 2), 2)
            result = f"あなたのBMIは {bmi_value} です"
        except (TypeError, ValueError, ZeroDivisionError):
            result = "入力エラー"
    return render(request, "work06/bmi.html", {"result": result})


def warikan(request):
    result = None
    if request.method == "POST":
        try:
            total = int(request.POST.get("total"))
            people = int(request.POST.get("people"))
            result = f"1人あたり {total // people} 円 (余り {total % people} 円)"
        except (TypeError, ValueError, ZeroDivisionError):
            result = "入力エラー"
    return render(request, "work06/warikan.html", {"result": result})


def chokin(request):
    result = None
    if request.method == "POST":
        try:
            monthly = int(request.POST.get("monthly"))
            years = int(request.POST.get("years"))
            total = monthly * 12 * years
            result = f"{years} 年後の貯金額は {total:,} 円 です"
        except (TypeError, ValueError):
            result = "入力エラー"
    return render(request, "work06/chokin.html", {"result": result})


def calculator(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            op = request.POST.get("op")
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2 if num2 != 0 else "割れません"
        except (TypeError, ValueError, ZeroDivisionError):
            result = "入力エラー"
    return render(request, "work06/calculator.html", {"result": result})
