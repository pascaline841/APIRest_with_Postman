# Generated by Django 3.2.4 on 2021-06-22 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Read', 'Read')], default='Read', max_length=10),
        ),
    ]
