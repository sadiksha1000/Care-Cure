# Generated by Django 3.1.6 on 2021-03-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20210314_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]