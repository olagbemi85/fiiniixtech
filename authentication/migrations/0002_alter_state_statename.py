# Generated by Django 3.2.8 on 2023-11-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='stateName',
            field=models.CharField(max_length=225),
        ),
    ]
