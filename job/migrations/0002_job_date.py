# Generated by Django 2.2.1 on 2020-03-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date',
            field=models.DateField(default='timezone.now'),
        ),
    ]
