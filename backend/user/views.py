from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Success")
        return Response("Failed")
