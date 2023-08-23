from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        """for password hashing"""
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name','age']
        # exclude = ['id']

    # Custom validators
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'age can not be less than 18'})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': 'name cannot be numeric'})
                
        return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested Serializer
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1         # Nested Serializer
