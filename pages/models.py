from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f'{self.titulo} - por {self.autor.username}'
