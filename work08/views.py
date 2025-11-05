from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo


# 一覧画面
def index(request):
    memos = Memo.objects.all().order_by("-updated_at")
    return render(request, "memo/index.html", {"memos": memos})


# 新規作成
def new_memo(request):
    memo = Memo.objects.create(title="no title", content="")
    return redirect("edit", memo_id=memo.id)


# 編集画面
def edit(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == "POST":
        memo.title = request.POST.get("title", memo.title)
        memo.content = request.POST.get("content", memo.content)
        memo.save()
        return redirect("index")
    return render(request, "memo/edit.html", {"memo": memo})
