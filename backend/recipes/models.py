from django.db.models import *

class Category(Model):
    title = TextField()

class Recipe(Model):
    id = IntegerField(primary_key=True)
    category = ForeignKey(Category,on_delete=CASCADE)
    name = TextField()
    image = TextField()
    description = TextField()
    steps = TextField()
    username = TextField()
    category_title = TextField()