# Generated by Django 4.1.1 on 2022-12-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='e_desc',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='main',
            name='mdate',
            field=models.CharField(max_length=50),
        ),
    ]