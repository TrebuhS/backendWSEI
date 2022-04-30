from django.db import models

class UserModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()