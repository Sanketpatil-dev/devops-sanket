# Generated by Django 2.1.15 on 2022-11-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0003_auto_20221129_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookticket',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pemail', models.CharField(max_length=30)),
                ('pnum', models.CharField(max_length=13)),
                ('clocation', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('sdate', models.DateField()),
                ('adults', models.CharField(max_length=3)),
                ('child', models.CharField(max_length=3)),
            ],
        ),
    ]
