# Generated by Django 4.1.2 on 2023-07-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_ground',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
