# Generated by Django 4.0.5 on 2022-06-12 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_socialnetworkaccounts_account_platform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialNetworkAccounts',
            new_name='SocialNetworkAccount',
        ),
    ]
