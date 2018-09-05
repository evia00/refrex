from django.forms import ModelForm
from cms.models import User


class LoginForm(ModelForm):
    """ログインフォーム"""
    class Meta:
        model = User
        fields = ('userId', 'password')


class AddForm(ModelForm):
    """登録フォーム"""
    class Meta:
        model = User
        fields = ('userId', 'password')
