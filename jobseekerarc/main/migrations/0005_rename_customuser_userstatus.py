# Generated by Django 4.2.2 on 2023-07-25 19:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='UserStatus',
        ),
    ]
