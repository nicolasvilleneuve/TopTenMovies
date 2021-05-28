# Generated by Django 3.2.3 on 2021-05-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=10)),
                ('ranking', models.DecimalField(decimal_places=2, max_digits=5)),
                ('review', models.CharField(max_length=2000)),
                ('img_url', models.URLField()),
            ],
        ),
    ]