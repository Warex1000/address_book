from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Users
from django.forms import ModelForm, TextInput, FileInput, ImageField


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'country', 'city', 'street', 'url_users', 'phone', 'image']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'surname': TextInput(attrs={'placeholder': 'Фамилия пользователя'}),
            'country': TextInput(attrs={'placeholder': 'Страна'}),
            'city': TextInput(attrs={'placeholder': 'Город'}),
            'street': TextInput(attrs={'placeholder': 'Улица'}),
            'url_users': TextInput(attrs={'placeholder': 'URL пользователя'}),
            'phone': TextInput(attrs={'placeholder': 'Номер телефона'}),
        }
