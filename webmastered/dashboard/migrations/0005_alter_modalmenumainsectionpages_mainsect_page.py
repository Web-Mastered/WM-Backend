# Generated by Django 4.0.5 on 2022-06-09 19:42

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_modalmenumainsectionpages_mainsect_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalmenumainsectionpages',
            name='mainsect_page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modalmenu_mainsect_page', to='dashboard.websitesettings'),
        ),
    ]
