from rest_framework import serializers
from .models import Recipe,Category
class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length = 50)
    image = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 500)
    steps = serializers.CharField(max_length = 1000)
    username = serializers.CharField(max_length = 50)
    category_title = serializers.CharField(max_length = 50)
    class Meta:
        model = Recipe
        fields = ['id','category_id','name','image','description','steps','username','category_title']
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length = 100)
    class Meta:
        model = Category
        fields = ['title']