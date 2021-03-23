# Generated by Django 3.1.5 on 2021-03-22 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0015_auto_20210322_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=220),
            preserve_default=False,
        ),
    ]