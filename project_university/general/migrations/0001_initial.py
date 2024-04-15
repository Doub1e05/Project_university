from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='generalForStudent',
            fields=[
                ('idOfTeacher', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfTeacher', models.CharField(max_length=255)),
                ('nameOfDiscipline', models.CharField(max_length=255)),
                ('statusOfLab', models.BooleanField(default=False)),
                ('students', models.ManyToManyField( to='generalForStudent'))
            ],
        ),
        migrations.CreateModel(
            name='generalForTeacher',
            fields=[
                ('idOfStudent', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfStudent', models.CharField(max_length=255)),
                ('statusOfLab', models.BooleanField(default=False)),
                ('teachers', models.ManyToManyField(to='generalForTeacher'))
            ],
        ),
    ]