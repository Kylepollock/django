# Generated by Django 2.0.9 on 2018-10-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogAppointment',
            fields=[
                # ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # ('name', models.CharField(max_length=127)),
                # ('time', models.CharField(max_length=127)),
                # ('date', models.CharField(max_length=127)),
                # ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                # ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # ('first_name', models.CharField(max_length=127)),
                # ('last_name', models.CharField(default='', max_length=127)),
                # ('email', models.CharField(default='', max_length=127)),
                # ('phone', models.CharField(default='', max_length=127)),
                # ('address', models.CharField(default='', max_length=127)),
            ],
        ),
    ]
