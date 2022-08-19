from django.db import models

from apps.core.models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    surname = models.CharField(max_length=220, blank=False, null=False)
    nationality = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    state = models.BooleanField('State', default=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(BaseModel):
    title = models.CharField('Title', max_length=255, blank=False, null=False)
    publication_date = models.DateField('Publication Date', blank=False, null=False)
    editorial = models.DateField('Editorial', blank=False, null=False)
    state = models.BooleanField('State', default=True)

    """
    -1 libro solo puede tener 1 autor:
        autor_id = models.OneToOneField(Autor, on_delete=models.CASCADE)
    - 1 libro puede ser escrito por uno o mas autores:
        autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    - Muchos libros pueden ser escritos por uno o muchos autores:
    """
    author = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title
