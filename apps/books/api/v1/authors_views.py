from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from apps.books.models import Author
from apps.books.serializers.v1.authors_serializer import AuthorSerializer


class AuthorsListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer

    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        print(request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=422)


class AuthorsUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = AuthorSerializer.Meta.model.objects

    # permission_classes = [IsAuthenticated]

    def update(self, request, pk=None, *args, **kwargs):
        print(f'llave: {pk}')
        instance = self.serializer_class.Meta.model.objects.get(pk=pk)
        print('data', request.data)

        updated = self.serializer_class(
            instance,
            data=request.data
        )

        if updated.is_valid():
            updated.save()
            return JsonResponse(updated.data, status=200)
        else:
            return JsonResponse(updated.errors, status=200)
