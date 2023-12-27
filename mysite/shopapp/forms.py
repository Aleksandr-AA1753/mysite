from django import forms
from .models import Tovar


class TovarForm(forms.ModelForm):
    class Meta:
        # Эта форма будет работать с моделью Post
        model = Tovar
        # Поля модели, которые должны отображаться в веб-форме
        fields = '__all__'