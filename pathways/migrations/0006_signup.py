# Generated by Django 2.1.15 on 2022-11-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0005_auto_20221129_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=20)),
                ('emailid', models.CharField(max_length=30)),
                ('phnum', models.CharField(max_length=13)),
                ('pswd', models.CharField(max_length=8)),
            ],
        ),
    ]
