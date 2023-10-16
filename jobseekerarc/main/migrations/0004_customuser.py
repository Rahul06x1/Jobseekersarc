# Generated by Django 4.2.2 on 2023-07-25 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_jobrecruiter_jobseeker_delete_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_jobseeker', models.BooleanField(default=False, verbose_name='jobseeker status')),
                ('is_jobrecruiter', models.BooleanField(default=False, verbose_name='jobrecruiter status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
