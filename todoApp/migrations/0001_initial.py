# Generated by Django 3.0.2 on 2020-01-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_desc', models.TextField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
