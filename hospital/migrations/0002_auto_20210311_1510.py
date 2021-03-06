# Generated by Django 3.1.6 on 2021-03-11 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='static/uploads')),
                ('name', models.CharField(max_length=300, null=True)),
                ('description', models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(50)])),
                ('treatment_name', models.CharField(max_length=300, null=True)),
                ('treatment_description', models.CharField(max_length=2000, null=True, validators=[django.core.validators.MinLengthValidator(50)])),
            ],
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]
