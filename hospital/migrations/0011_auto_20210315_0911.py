# Generated by Django 3.1.6 on 2021-03-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_auto_20210315_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
