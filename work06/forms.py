# myapp/forms.py
from django import forms


class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(
        label="令和（年）", min_value=1, help_text="例: 5 → 令和5年"
    )
