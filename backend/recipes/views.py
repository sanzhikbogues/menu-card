from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe,Category
from json import loads
from .serializers import RecipeSerializer,CategorySerializer

@api_view()
def GetAll(request):
    return Response(RecipeSerializer(Recipe.objects.all(),many = True).data)
@api_view(["post"])
def Create(request):
    data = loads(request.body)
    Recipe.objects.create(category_title=Category.objects.get(pk=data['category_id']).title,id = 500,category = Category.objects.get(pk=data['category_id']),name = data['name'],image = data['image'],description = data['description'],steps = data['steps'],username = data['username'])
    return Response("OK")
@api_view()
def GetCategoryById(request,id):
    return Response(CategorySerializer(Category.objects.get(pk=id)).data)