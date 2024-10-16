# Generated by Django 4.1 on 2024-03-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ulifeapp", "0008_fcmtoken"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="keyword",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="keyword",
            constraint=models.UniqueConstraint(
                fields=("name", "host"), name="unique_name_host"
            ),
        ),
    ]
