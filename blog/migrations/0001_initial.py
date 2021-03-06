# Generated by Django 2.2.1 on 2020-03-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/image/')),
            ],
        ),
    ]
