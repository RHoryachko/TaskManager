import datetime

from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.forms.widgets import DateTimeInput


class HashtagValidator:
    '''Валідатор хештегу'''
    def __call__(self, value):
        if not value.startswith('#'):
            raise ValidationError('Хештег повинен починатися з символу #')


class FutureDateValidator:
    '''Валідатор дедлайну'''
    def __call__(self, value):
        if isinstance(value, datetime.date):
            # Перетворення offset-naive datetime в offset-aware datetime
            value = timezone.make_aware(datetime.datetime.combine(value, datetime.datetime.min.time()))

        if value <= timezone.now():
            raise ValidationError('Дата повинна бути у майбутньому')


class TaskForm(forms.ModelForm):
    '''Форма таски'''

    hashtag = forms.CharField(max_length=50, required=False, validators=[HashtagValidator()])
    deadline = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}), 
                                    validators=[FutureDateValidator()], required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'hashtag', 'status']
        