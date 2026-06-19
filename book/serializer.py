from rest_framework import serializers
from .models import book
from author.serializer import Authorserializers
class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=book
        fields='__all__'

class BookAuthor(serializers.ModelSerializer):
    author= Authorserializers(read_only=True)
    class Meta:
        model=book
        fields='__all__'        