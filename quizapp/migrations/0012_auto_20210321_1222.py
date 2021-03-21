# Generated by Django 3.1.5 on 2021-03-21 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0011_quiz_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=220),
            preserve_default=False,
        ),
    ]