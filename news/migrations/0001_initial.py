# Generated by Django 3.2 on 2021-04-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date_published', models.DateTimeField()),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]
