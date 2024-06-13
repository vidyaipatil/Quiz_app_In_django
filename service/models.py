# from django.db import models

# Create your models here.
from django.db import models
class Service1(models.Model):
    question=models.TextField()
    answer=models.CharField(max_length=100)
    solution=models.TextField()
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)
    

# Create your models here.
