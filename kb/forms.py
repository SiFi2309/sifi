from django import forms
from django.core.validators import RegexValidator


class UserForm(forms.Form):
    name = forms.CharField(label="Им'я")
    subn = forms.CharField(label="Прізвище")
    firstn = forms.CharField(label="Ім'я по батькові ")
    age = forms.IntegerField(label="Вік ")
    niin = forms.IntegerField(label="Номер Інн ")
    nump = forms.IntegerField(label="Номер Паспорту ")
    email = forms.EmailField(label="Пошта ")
    password = forms.CharField(label="Пароль")
    addn = forms.CharField(label="Номер для переводу")
    kg = forms.CharField(label="Перевести (грн)")
