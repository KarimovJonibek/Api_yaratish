from .models import Books
from rest_framework import serializers

class BoockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'content', 'author')



