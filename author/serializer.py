from rest_framework import serializers
from .models import author

class Authorserializers(serializers.ModelSerializer):
    class Meta:
        model=author
        fields='__all__'