# Generated by Django 4.0.1 on 2022-02-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user1', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Truck'), (4, 'SUV')])),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
