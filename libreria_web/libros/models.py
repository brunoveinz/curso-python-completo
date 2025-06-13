from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre  = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    titulo              = models.CharField(max_length=200)
    autor               = models.CharField(max_length=100)
    fecha_publicacion   = models.DateField()
    isbn                = models.CharField(max_length=13, unique=True)
    genero              = models.CharField(max_length=50)
    categoria           = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros', null=True, blank=True)

    def __str__(self):
        return  self.titulo 
    
