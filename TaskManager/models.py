from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
	'''Модель таски'''
	PRIORITY_CHOICES = [
        ('Важливе', 'Важливе'),
        ('Середнє', 'Середнє'),
        ('Не важливе', 'Не важливе'),
    ]

	STATUS_CHOICES = [
        ('Задано', 'Задано'),
        ('В процесі', 'В процесі'),
        ('Виконано', 'Виконано'),
	]

	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	deadline = models.DateTimeField(blank=True, null=True)
	priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Не важливе')
	hashtag = models.CharField(max_length=50, blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Задано')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
