# Generated by Django 4.1 on 2024-03-04 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ulifeapp", "0009_alter_keyword_unique_together_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fcmtoken",
            name="fcm_token",
        ),
    ]
