import os
from random import randint
from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = randint(1, 1000)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'media/clients_photos/{new_filename}/{final_filename}'


class User(models.Model):
    featured = models.BooleanField('Destaque', default=False)
    first_name = models.CharField('Nome', max_length=30)
    last_name = models.CharField('Sobrenome', max_length=30)
    slug = models.SlugField('Nome Fantasia', max_length=30)
    age = models.PositiveIntegerField('Idade')
    description = models.TextField('Descrição', max_length=250)
    profile_picture = models.ImageField('Foto do Perfil', upload_to=upload_image_path)
    cacheForHours = models.DecimalField('Cachê/Hr', max_digits=6, decimal_places=2)
    weight = models.FloatField('Peso(kg)')
    height = models.FloatField('Altura(m)')
    bust = models.FloatField('Busto(cm)')
    waist = models.FloatField('Cintura(cm)')
    butt = models.FloatField('Bunda(cm)')

    created = models.DateTimeField('Criado em ', auto_now_add=True)
    modified = models.DateTimeField('Modificado em ', auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
