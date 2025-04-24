from django.urls import path
from .views import GetAll,Create,GetCategoryById


urlpatterns = [
    path('recipes/',GetAll),
    path('recipes/create/',Create),
    path('categories/<int:id>/',GetCategoryById),
]
