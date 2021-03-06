# Generated by Django 4.0 on 2022-01-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=20)),
                ('job_amount', models.IntegerField()),
                ('job_description', models.CharField(max_length=300)),
                ('job_duration', models.CharField(max_length=30)),
                ('job_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
