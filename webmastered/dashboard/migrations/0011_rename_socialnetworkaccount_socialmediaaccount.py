# Generated by Django 4.0.5 on 2022-06-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_rename_socialnetworkaccounts_socialnetworkaccount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialNetworkAccount',
            new_name='SocialMediaAccount',
        ),
    ]
