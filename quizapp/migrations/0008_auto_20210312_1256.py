# Generated by Django 3.1.5 on 2021-03-12 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0007_auto_20210312_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.choice'),
        ),
    ]