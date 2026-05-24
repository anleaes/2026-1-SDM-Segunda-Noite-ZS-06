from .models import Person
from rest_framework import serializers
from .models import Developer

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'