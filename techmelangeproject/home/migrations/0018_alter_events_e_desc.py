# Generated by Django 4.1.1 on 2023-01-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_studcoor_s_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='e_desc',
            field=models.CharField(max_length=2000),
        ),
    ]