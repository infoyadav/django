# Generated by Django 4.0.1 on 2022-02-14 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_remove_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='staff',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
