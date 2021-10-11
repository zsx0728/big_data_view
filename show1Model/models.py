from django.db import models

# Create your models here.

class show1_month_plan(models.Model):
    complete = models.CharField(max_length=20)
    plan = models.CharField(max_length=20)
