# Generated by Django 4.2.2 on 2023-07-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_jobapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_id', models.CharField(max_length=1)),
                ('resume', models.FileField(upload_to='store/pdfs/')),
            ],
        ),
    ]