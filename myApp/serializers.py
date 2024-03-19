from django.contrib.auth.models import Group, User
from rest_framework import serializers
from myApp.models import Products

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product_name', 'product_value', 'product_image', 'product_description']
