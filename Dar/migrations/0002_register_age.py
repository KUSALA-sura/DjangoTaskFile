# Generated by Django 3.0 on 2021-06-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='age',
            field=models.IntegerField(default=False),
        ),
    ]
