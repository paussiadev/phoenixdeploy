from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    linguagem = [
        ('pt-br', 'Português - Brasil'),
        ('eng', 'Inglês (Indisponível)')
    ]

    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    # profile_picture = models.ImageField(upload_to='fotos/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    idioma = models.CharField(verbose_name="Valor", null=False, blank=False,  choices=linguagem, default='pt-br', max_length=7)

    def __str__(self):
        return self.username
