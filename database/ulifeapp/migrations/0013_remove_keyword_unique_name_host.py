# Generated by Django 4.1 on 2024-03-07 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ulifeapp", "0012_alter_fcmtoken_keyword"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="keyword",
            name="unique_name_host",
        ),
    ]
