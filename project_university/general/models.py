from django.db import models
class generalForStudent(models.Model):
    idOfStudent = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameOfStudent = models.CharField(max_length=255)
    statusOfLab = models.BooleanField(default=False)

class generalForTeacher(models.Model):
    idOfTeacher = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameOfTeacher = models.CharField(max_length=255)
    nameOfDiscipline = models.CharField(max_length=255)
    statusOfLab = models.BooleanField(default=False)
