# Generated by Django 2.0.4 on 2018-05-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_show_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='shirt_size',
        ),
        migrations.AlterField(
            model_name='registration',
            name='company',
            field=models.CharField(blank=True, max_length=255, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='food_allergies',
            field=models.CharField(blank=True, max_length=255, verbose_name='Dietary requirements'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='github_nickname',
            field=models.CharField(blank=True, max_length=255, verbose_name='Github nickname'),
        ),
    ]
