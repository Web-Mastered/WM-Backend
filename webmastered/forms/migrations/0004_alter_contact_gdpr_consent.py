# Generated by Django 4.0.5 on 2022-06-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_alter_contact_marketing_consent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gdpr_consent',
            field=models.BooleanField(),
        ),
    ]
