from django.db import models
from django.contrib.auth.models import User

class masterClass(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    date = models.DateField()
    duration = models.IntegerField()
    location = models.TextField()
    description = models.TextField()
    image = models.TextField()
    price = models.TextField()
    maxAttendees = models.IntegerField()
    participants = models.IntegerField()
    createdUser = models.TextField()