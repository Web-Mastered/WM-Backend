# Generated by Django 4.0.5 on 2022-06-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='marketing_consent',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
