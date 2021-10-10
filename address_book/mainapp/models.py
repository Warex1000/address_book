import re
from django.db import models
from django.core.exceptions import ValidationError
'''
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
'''

'''
Создаем модель для адресной книги: Users
Поля модели:
Имя, фамилия (обязательные поля, уникальная комбинация) +
Адрес (Страна, Город, Улица) (опциональные поля) +
URL (опциональное поле, с валидацией) +
Телефон +
Изображение (опциональное поле, метод хранения произвольный) +
'''

# Функции:
# AddUser
# EditUser
# DeleteUser
# SearchUser


class Users(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия пользователя')
    country = models.CharField(max_length=30, verbose_name='Страна', blank=True)
    city = models.CharField(max_length=30, verbose_name='Город', blank=True)
    street = models.CharField(max_length=30, verbose_name='Улица', blank=True)
    url_users = models.URLField(max_length=200, verbose_name='URL пользователя', blank=True, unique=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    image = models.ImageField(verbose_name='Изображение', blank=True)
    # pip3 install pillow - for ImageField

    def __str__(self):
        return self.surname

    @staticmethod
    def validate_phone_number(phone):
        regex = r'^\+?1?\d{9,15}$'    # Пересмотреть регулярные выражения, фильтруют не так!
        if not re.match(regex, phone):
            raise ValidationError('Wrong phone number format.')

    @staticmethod
    def validate_username(url_users):
        regex = r'^([a-zA-Z]{4}[\w]{1,16})$'    # Пересмотреть регулярные выражения, фильтруют не так!
        if not re.match(regex, url_users):
            raise ValidationError('Wrong URL format.')

    class Meta:
        unique_together = ('name', 'surname')


'''
python3 manage.py makemigrations - Django использует миграции для переноса изменений в моделях (добавление поля, удаление модели и т.д.) на структуру базы данных.
python3 manage.py migrate
python3 manage.py runserver - run server
'''