from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator



class generalForTeacher(models.Model):
    idOfTeacher = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameOfTeacher = models.CharField(max_length=255)
    nameOfDiscipline = models.CharField(max_length=255)
    statusOfLab = models.BooleanField(default=False)

class Lab(models.Model):
     lab_id =  models.IntegerField()
     is_completed = models.BooleanField(default=False)

class UserManager(BaseUserManager):

    def create_user(self, login, last_name, first_name, surname, role, password=None):
        """
        Создание обычного польователя. Данные - логин и пароль
        """
        if not login:
            raise ValueError("Пользователь должен иметь логин")

        user = self.model(
            login=login,
            last_name = last_name,
            first_name = first_name,
            surname = surname,
            role = role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, last_name, first_name, surname, role, password=None):
        """
        Создание администратора. Данные - логин и пароль
        """
        user = self.create_user(
            login,
            password=password,
            last_name = last_name,
            first_name = first_name,
            surname = surname,
            role = role,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    login = models.CharField(
        verbose_name='Логин',
        max_length=30,
        unique=True,
    )

    last_name = models.CharField(
        blank=False, 
        max_length=255, 
        verbose_name='Фамилия'
        )
    
    first_name = models.CharField(
        blank=False, 
        max_length=255, 
        verbose_name='Имя'
        )
    
    surname = models.CharField(
        blank=True, 
        max_length=255, 
        verbose_name='Отчество'
        )
    
    role = models.CharField(
        choices = (
            ('Teacher', 'Преподаватель'),
            ('Student', 'Студент'),
            ), 
        max_length=7, 
        verbose_name='Должность', 
        blank=False
        )
    
    thread = models.ForeignKey(
        to='Thread',
        on_delete=models.PROTECT,
        verbose_name='Поток',
        null=True,
    )

    is_admin = models.BooleanField(default=False, verbose_name='Администрирование')

    objects = UserManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["last_name", "first_name", "surname", "role"]

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        "Есть ли у пользователя определенное разрешение?"
 
        return True

    def has_module_perms(self, app_label):
        "Есть ли у пользователя разрешения на просмотр приложения app_label?"

        return True

    @property
    def is_staff(self):
        "Является ли пользователь администратором?"
 
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
class Thread(models.Model):
    thread = models.CharField(
        blank=True, 
        max_length=5,
        default="",
        verbose_name='Направление (Например, ИВТб)',
        validators=[RegexValidator(regex=r'^[а-яА-я]+$')]
        )
    
    course = models.CharField(
        blank=True,
        max_length=1,
        null=True,
        choices=(
            ('1', '1'),
            ('2', '2'), 
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        ),
        verbose_name='Курс',
        )
    
    def __str__(self):
        return f'{self.thread}-{self.course}'
    
    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'
