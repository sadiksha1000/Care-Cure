# Generated by Django 3.1.6 on 2021-03-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20210311_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=300, null=True)),
                ('doctor_designation', models.CharField(max_length=300, null=True)),
                ('doctor_image', models.ImageField(blank=True, null=True, upload_to='static/uploads')),
                ('doctor_schedule', models.CharField(max_length=200, null=True)),
                ('work_experience', models.CharField(max_length=5000, null=True)),
                ('doctor_background', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='static/uploads'),
        ),
    ]
