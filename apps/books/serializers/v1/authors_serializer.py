from rest_framework import serializers

from apps.books.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'surname',
            'nationality',
            'description',
            'state',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
        }
