# Generated by Django 3.0.2 on 2020-01-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='doc',
            field=models.FileField(default='docs/none/none.txt', upload_to='docs/'),
        ),
    ]