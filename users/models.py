from django.contrib.auth.models import AbstractUser
from django.db import models

NB = {'blank': True, 'null': True}


class User(AbstractUser):

    username = models.CharField(max_length=30,
                                unique=True,
                                verbose_name='username')

    email = models.EmailField(unique=True, verbose_name='Email', **NB)

    phone = models.CharField(max_length=30, verbose_name='phone number', **NB)
    country = models.CharField(max_length=30, verbose_name='country', **NB)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NB)
    last_login = models.DateField(verbose_name='Last authentication',
                                  default='2023-01-01')
    is_sub = False
    chat_id = models.IntegerField(unique=True, verbose_name='tg chat id', **NB)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
