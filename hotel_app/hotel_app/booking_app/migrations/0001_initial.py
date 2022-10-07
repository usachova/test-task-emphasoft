# Generated by Django 4.0.4 on 2022-10-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('cost', models.IntegerField()),
                ('beds_count', models.IntegerField()),
            ],
        ),
    ]
