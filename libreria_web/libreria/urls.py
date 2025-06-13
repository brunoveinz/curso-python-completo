from django.contrib import admin
from django.urls import path
from libros.views import vista_principal, vista_categorias, vista_libros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_principal, name="home"),
    path('libros/', vista_libros, name="libros"),
    path('categorias/', vista_categorias, name="categorias"),

]
