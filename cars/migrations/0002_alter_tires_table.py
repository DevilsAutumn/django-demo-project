# Generated by Django 5.0.dev20230224125942 on 2023-02-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tires", "0001_initial"),
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="tires",
            table="tires_tires",
        ),
    ]
