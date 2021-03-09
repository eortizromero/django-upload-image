from django.db import models


class Images(models.Model):

    titulo = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    descripcion = models.TextField(default="")

    def __str__(self):
        return self.titulo
