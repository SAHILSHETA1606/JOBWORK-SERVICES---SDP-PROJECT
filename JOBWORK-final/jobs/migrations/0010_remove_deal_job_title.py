# Generated by Django 4.0 on 2022-02-26 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_deal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='job_title',
        ),
    ]
