from rest_framework import serializers
from .models import file

class Fileserializers(serializers.ModelSerializer):
    class Meta:
        model=file
        fields='__all__'