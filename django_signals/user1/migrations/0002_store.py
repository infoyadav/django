# Generated by Django 4.0.1 on 2022-02-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30, unique=True)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
                'permissions': (('give_refund', 'Can refund customers'), ('can_hire', 'Can hire employees')),
                'default_permissions': ('add',),
            },
        ),
    ]