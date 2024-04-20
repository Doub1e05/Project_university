from django.db import models

class Lab(models.Model):
     lab_id =  models.IntegerField()
     is_completed = models.BooleanField(default=False)