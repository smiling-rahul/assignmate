# Generated by Django 2.0.1 on 2018-03-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='option_a',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='questions',
            name='option_b',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='questions',
            name='option_c',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='questions',
            name='option_d',
            field=models.CharField(default=0, max_length=200),
        ),
    ]