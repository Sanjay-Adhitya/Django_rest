from pyexpat import model
from django.db import models

# Create your models here.
class Member(models.Model):
    Member_id = models.AutoField(primary_key=True)
    Member_name = models.CharField(max_length=200)

class Fund(models.Model):
    Fund_id = models.AutoField(primary_key=True)
    Fund_data = models.JSONField(max_length=5000)