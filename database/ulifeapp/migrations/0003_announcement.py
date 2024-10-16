# Generated by Django 4.1 on 2023-05-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ulifeapp", "0002_alter_meal_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("major", models.CharField(max_length=15)),
                ("nid", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=500)),
                ("url", models.CharField(max_length=1000)),
                ("date_post", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "elec_general",
                "managed": False,
            },
        ),
    ]
