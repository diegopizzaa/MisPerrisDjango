from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):

    POST_CHOISES = (
        ('Disponible', 'Disponible'),
        ('Rescatado', 'Rescatado'),
        ('Adoptado', 'Adoptado')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    thumb = models.ImageField(default='default.png', blank=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    slug = models.SlugField()
    descripcion = models.TextField(max_length=200)
    raza = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    estado = estado = models.CharField(max_length = 100, blank=True, null=True, choices = POST_CHOISES)

    def __str__(self):
        return self.nombre

    def snippet(self):
        return self.descripcion[:50] + '...'  
    # python manage.py makemigrations 
    # python manage.py migrate
