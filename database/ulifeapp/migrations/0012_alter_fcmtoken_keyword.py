# Generated by Django 4.1 on 2024-03-07 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ulifeapp", "0011_rename_keyword_name_fcmtoken_keyword_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fcmtoken",
            name="keyword",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fcm_tokens",
                to="ulifeapp.keyword",
            ),
        ),
    ]
