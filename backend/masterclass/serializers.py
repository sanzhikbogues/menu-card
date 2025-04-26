from rest_framework import serializers
from .models import masterClass

class masterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = masterClass
        fields = ['name','date','duration','location','description','image','price','maxAttendees','participants']
    def create(self,data):
        return masterClass.objects.create(**data)