from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import masterClass
from .serializers import masterClassSerializer

class masterClassView(APIView):
    def post(self,request):
        data = request.data
        serializer = masterClassSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response("Successfully added")
        return Response("Failed to add")
    def get(self,request):
        return Response(masterClassSerializer(masterClass.objects.all(),many=True).data)
@api_view(['get','put','delete'])
def GetMasterClassById(request,id):
    if request.method == 'GET':
        return Response(masterClassSerializer(masterClass.objects.get(pk=id)).data)
    if request.method == 'PUT':
        data = request.data
        masterclass = get_object_or_404(masterClass,id=id)
        for field,value in data.items():
            print(field,value)
            setattr(masterclass,field,value)
        masterclass.save()
        return Response("OK")
    if request.method =='DELETE':
        masterclass = get_object_or_404(masterClass,id=id)
        masterclass.delete()
        return Response("Deleted successfully")