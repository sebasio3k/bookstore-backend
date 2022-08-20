from django.db.models import Prefetch, Q
from rest_framework import serializers

from apps.books.models import Book, Author
from apps.books.serializers.v1.authors_serializer import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    author_detail = serializers.SerializerMethodField('get_author', read_only=True)

    def get_author(self, book):
        try:
            qs = Author.objects.filter(book__pk=book.id)
            print('qs', qs)
            return AuthorSerializer(qs, many=True).data
        except:
            return []

    def create(self, validated_data):
        print('entra')
        print(f'validate_data {validated_data}')
        del validated_data['author']
        print(f'validate_data {validated_data}')

        print('create')
        try:
            authors_ids = self.initial_data['author']
            print('authors_ids', authors_ids)
            for item in range(len(authors_ids)):
                authors_ids[item] = int(authors_ids[item].strip())  # quitar espacios
                authors_ids[item] = int(authors_ids[item])  # Convertir str a int
                exist = Author.objects.get(pk=authors_ids[item])  # validar si la cateforia existex
            print('authors_ids 2', authors_ids)

            # validated_data['author'] = authors
            print('sentencia')
            new_book = Book.objects.create(**validated_data)
            print('fin sentencia')

            if authors_ids:
                for id in list(authors_ids):
                    print('id', id, type(id))
                    new_book.author.add(id)
            # new_post.save()
            return new_book

        except Exception as e:
            raise serializers.ValidationError({'detail': e})

        validated_data['author_id'] = self.context.get('author').id
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Updates only the manytomany relationshio in book and author """
        try:
            print('entra uptare try')
            authors_ids = self.initial_data['author']
            # authors_ids = self.initial_data['author']
            print('authors_ids', authors_ids)
            for item in range(len(authors_ids)):
                authors_ids[item] = int(authors_ids[item].strip())  # quitar espacios
                # authors_ids[item] = int(authors_ids[item])  # Convertir str a int
                exist = Author.objects.get(pk=authors_ids[item])  # validar si la cateforia existe
            print('authors_ids fin', authors_ids)

            instance.author.set(authors_ids)
            return instance

        except Exception as e:
            raise serializers.ValidationError({'detail': e})

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'publication_date',
            'cover',
            'description',
            'editorial',
            'state',
            'author',
            'author_detail',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
        }


class BookInfoUpdateSerializer(serializers.ModelSerializer):
    author_detail = serializers.SerializerMethodField('get_author', read_only=True)

    def get_author(self, book):
        try:
            qs = Author.objects.filter(book__pk=book.id)
            print('qs', qs)
            return AuthorSerializer(qs, many=True).data
        except:
            return []

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'publication_date',
            'cover',
            'description',
            'editorial',
            'state',
            # 'author',
            'author_detail',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
        }
