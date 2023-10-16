# Generated by Django 4.2.2 on 2023-07-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='store/pdfs/')),
            ],
        ),
    ]