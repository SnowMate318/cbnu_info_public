# Generated by Django 4.1 on 2023-05-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cieat",
            fields=[
                ("article_idx", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=500)),
                ("state", models.CharField(max_length=20)),
                ("art_organization", models.CharField(max_length=200, null=True)),
                ("recruit_time", models.CharField(max_length=50)),
                ("recruit_time_start", models.DateTimeField(blank=True, null=True)),
                ("recruit_time_close", models.DateTimeField(blank=True, null=True)),
                ("part_class", models.CharField(max_length=1000)),
                ("part_grade", models.CharField(max_length=20)),
                ("category", models.CharField(max_length=500)),
                ("score", models.FloatField()),
                ("point", models.IntegerField()),
                ("htmlpath", models.CharField(max_length=1000)),
            ],
            options={
                "db_table": "article",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Extracur",
            fields=[
                ("category", models.CharField(max_length=15)),
                ("category_sub", models.CharField(max_length=30)),
                ("url", models.CharField(max_length=1000)),
                ("post_id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=500)),
                ("post_organization", models.CharField(max_length=200)),
                ("startdate", models.DateField(blank=True)),
                ("closingdate", models.DateTimeField(blank=True, null=True)),
                ("apply_url", models.CharField(max_length=1000)),
                ("hits", models.IntegerField()),
                ("img_url", models.CharField(max_length=1000)),
                ("img_filepath", models.CharField(max_length=1000)),
                ("img_thumbnail_url", models.CharField(max_length=1000)),
                ("img_thumbnail_filepath", models.CharField(max_length=1000)),
            ],
            options={
                "db_table": "post",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Meal",
            fields=[
                ("menu_date", models.DateField(blank=True, null=True)),
                ("food_time", models.CharField(max_length=10)),
                ("cafeteria_name", models.CharField(max_length=5)),
                ("food_name", models.CharField(max_length=30)),
                ("food_idx", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "meal",
                "managed": False,
            },
        ),
    ]
