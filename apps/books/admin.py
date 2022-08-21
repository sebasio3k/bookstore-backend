from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


# class CategoriaResource(resources.ModelResource):
#     class Meta:
#         model = Categoria

# class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     # Barra de busqueda:
#     search_fields = ['nombre', 'estado']
#     # Para atributos en vista de registros:
#     list_display = ['id', 'nombre', 'estado', 'fecha_creacion']
#     resource_class = CategoriaResource

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Barra de busqueda:
    search_fields = ['name', 'surname', 'state', 'nationality']
    # Para atributos en vista de registros:
    list_display = [
        'id',
        'name',
        'surname',
        'nationality',
        'description',
        'state',
    ]
    resource_class = AuthorResource


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'title', 'publication_date', 'description', 'editorial', 'state']
    list_display = [
        'id',
        'title',
        'publication_date',
        'cover',
        'description',
        'editorial',
        'state',
    ]
    resource_class = BookResource


# Register your models here.
# admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
