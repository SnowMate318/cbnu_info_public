# Generated by Django 4.1 on 2024-03-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ulifeapp", "0010_remove_fcmtoken_fcm_token"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fcmtoken",
            old_name="keyword_name",
            new_name="keyword",
        ),
        migrations.RemoveField(
            model_name="fcmtoken",
            name="uid",
        ),
        migrations.AddField(
            model_name="fcmtoken",
            name="fcm_token",
            field=models.CharField(default="", max_length=1000),
            preserve_default=False,
        ),
    ]
