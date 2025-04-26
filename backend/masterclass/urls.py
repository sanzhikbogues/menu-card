from django.urls import path
from .views import masterClassView,GetMasterClassById


urlpatterns = [
    path('masterclass/',masterClassView.as_view()),
    path('masterclass/create/', masterClassView.as_view()),
    path('masterclass/<int:id>/', GetMasterClassById)

]
