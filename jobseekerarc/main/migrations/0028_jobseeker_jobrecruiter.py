# Generated by Django 4.2.2 on 2023-08-05 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0027_delete_jobrecruiter_delete_jobseeker_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('is_jobseeker', models.BooleanField(default=False, verbose_name='jobseeker status')),
                ('is_jobrecruiter', models.BooleanField(default=False, verbose_name='jobrecruiter status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobRecruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('is_jobseeker', models.BooleanField(default=False, verbose_name='jobseeker status')),
                ('is_jobrecruiter', models.BooleanField(default=False, verbose_name='jobrecruiter status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]