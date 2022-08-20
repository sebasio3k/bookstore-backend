from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from apps.books.models import Book, Author
from apps.books.serializers.v1.book_serializer import BookSerializer, BookInfoUpdateSerializer


class BooksListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer

    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data={
                'title': request.data.get('title', None),
                'publication_date': request.data.get('publication_date', None),
                'cover': request.data.get('cover', None),
                'description': request.data.get('description', None),
                'editorial': request.data.get('editorial', None),
                'state': request.data.get('state', None),
                'author': request.data['author'].split(',')
            },
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=422)


class BooksUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = BookSerializer.Meta.model.objects

    # permission_classes = [IsAuthenticated]

    def update(self, request, pk=None, *args, **kwargs):
        print(f'llave: {pk}')
        instance = self.serializer_class.Meta.model.objects.get(pk=pk)
        print('data', request.data)

        updated_relationship = BookSerializer(
            instance,
            data={
                'title': request.data.get('title', None),
                'publication_date': request.data.get('publication_date', None),
                'cover': request.data.get('cover', None),
                'description': request.data.get('description', None),
                'editorial': request.data.get('editorial', None),
                'state': request.data.get('state', None),
                'author': request.data['author'].split(',')
            },
        )
        updated_book_info = BookInfoUpdateSerializer(
            instance, data=request.data
        )

        if updated_book_info.is_valid():
            updated_book_info.save()
            if updated_relationship.is_valid():
                updated_relationship.save()
                return JsonResponse(updated_relationship.data, status=200)
            else:
                print('else 2')
                return JsonResponse(updated_relationship.errors, status=200)
        else:
            return JsonResponse(updated_book_info.errors, status=200)
