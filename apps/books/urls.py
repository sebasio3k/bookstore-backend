from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.books.api.v1.authors_views import AuthorsListCreateView, AuthorsUpdateRetrieveDeleteView
from apps.books.api.v1.books_views import BooksListCreateView, BooksUpdateRetrieveDeleteView

urlpatterns = [
    # Authors
    path('api/v1/authors', AuthorsListCreateView.as_view(), name='list_create_author'),
    path('api/v1/authors/<int:pk>', AuthorsUpdateRetrieveDeleteView.as_view(), name='manage_author'),
    # path('list-author/', login_required(ListadoAutores.as_view()), name='listar_autor'),
    # path('crear-autor/', login_required(CrearAutor.as_view()), name='crear_autor'),
    # # path('inicio_autor/', InicioAutor.as_view(), name='inicio_autor'),
    # path('editar-autor/<int:pk>', login_required(ActualizarAutor.as_view()), name='editar_autor'),
    # path('eliminar-autor/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar_autor'),
    # Books
    path('api/v1/books', BooksListCreateView.as_view(), name='list_create_books'),
    path('api/v1/books/<int:pk>', BooksUpdateRetrieveDeleteView.as_view(), name='manage_author'),
    # path('listar-libro/', login_required(ListadoLibros.as_view()), name='listar_libro'),
    # path('crear-libro/', login_required(CrearLibro.as_view()), name='crear_libro'),
    # path('editar-libro/<int:pk>', login_required(ActualizarLibro.as_view()), name='editar_libro'),
    # path('eliminar-libro/<int:pk>', login_required(EliminarLibro.as_view()), name='eliminar_libro'),
]
