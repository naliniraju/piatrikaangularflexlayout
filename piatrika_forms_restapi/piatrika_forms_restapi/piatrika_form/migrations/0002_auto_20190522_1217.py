# Generated by Django 2.1.7 on 2019-05-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piatrika_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='division_id',
            field=models.CharField(max_length=20),
        ),
    ]
