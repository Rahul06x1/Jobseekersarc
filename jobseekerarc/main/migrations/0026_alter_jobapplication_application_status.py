# Generated by Django 4.2.2 on 2023-07-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='application_status',
            field=models.CharField(default='status_pending', max_length=20),
        ),
    ]
