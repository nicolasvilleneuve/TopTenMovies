# Generated by Django 3.2.3 on 2021-06-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_ten', '0002_auto_20210606_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]