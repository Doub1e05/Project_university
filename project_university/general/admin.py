from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.admin import ModelAdmin

# Пользовательские модели
from .models import Status, User, Thread, Works, Subjects

class StatusAdmin(ModelAdmin):
    list_display = ['work', 'student', 'status', 'identifier']
    list_editable = ['status']
    
    def has_add_permission(self, request):
        return False

class WorksAdmin(ModelAdmin):
    list_display = ['work_name', 'thread', 'subject']

class SubjectsAdmin(ModelAdmin):
    list_display = ['subject_name']

class UserCreationForm(forms.ModelForm):
    """
    Форма для создания новых пользователей. Включает в себя все необходимое
    поля, а также повторный пароль
    """

    password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Подтвердите пароль", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["login", "first_name", "last_name", "surname", "role"]

    def clean_password2(self):
        """
        Проверка на совпадение полей пароля
        """

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают!")
        
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    """
    Форма для редактирования пользователей
    """

    password = ReadOnlyPasswordHashField(label=("Пароль"))

    class Meta:
        model = User
        fields = ["login", "password", "last_name", "first_name", "surname", "role", "thread", "telegram", "is_admin"]


class UserAdmin(BaseUserAdmin):

    # Формы для добавления и изменения экземпляров пользователей
    form = UserChangeForm
    add_form = UserCreationForm

    # Поля, которые будут использоваться при отображении модели пользователя.
    # Они переопределяют определения в базовом UserAdmin, которые ссылаются на определенные поля в auth.User.
    list_display = ["login", "last_name", "first_name", "surname", "role", "telegram", "thread"]
    list_filter = ["is_admin"]
    list_editable = ["telegram", "thread"]

    fieldsets = [
        ("Учётная запись", {"fields": ["login", "password"]}),
        ("Персональная информация", {"fields": ["last_name", "first_name", "surname", "role", "thread"]}),
        ("Прочее", {"fields": ["telegram", "is_admin", "last_login"]}),
    ]

    def clean(self):
        cleaned_data = super(UserAdmin, self).clean()
        print(cleaned_data.get('role'))

    # add_fieldsets не является стандартным атрибутом ModelAdmin.
    # UserAdmin переопределяет get_fieldsets для использования этого атрибута при создании пользователя.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["login", "last_name", "first_name", "surname", "role", "password1", "password2"],
            },
        ),
    ]
    
    readonly_fields = ["last_login"]
    search_fields = ["login", "last_name", "first_name", "surname", "thread", "telegram"]
    ordering = ["login"]
    filter_horizontal = []


# Регистрация нового UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Thread)
admin.site.register(Status, StatusAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Works, WorksAdmin)

# Поскольку мы не используем встроенные разрешения Django, отменяем регистрацию модели группы от администратора.
admin.site.unregister(Group)
