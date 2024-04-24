from django.db import models

<<<<<<< HEAD
class generalForTeacher(models.Model):
    idOfTeacher = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameOfTeacher = models.CharField(max_length=255)
    nameOfDiscipline = models.CharField(max_length=255)
    statusOfLab = models.BooleanField(default=False)
||||||| 2c8de9b
class generalForTeacher(models.Model):
    idOfTeacher = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameOfTeacher = models.CharField(max_length=255)
    nameOfDiscipline = models.CharField(max_length=255)
    statusOfLab = models.BooleanField(default=False)
=======
class Lab(models.Model):
     lab_id =  models.IntegerField()
     is_completed = models.BooleanField(default=False)
>>>>>>> b6f97531d08ebe10880f7635b4ca352c0cc97002
