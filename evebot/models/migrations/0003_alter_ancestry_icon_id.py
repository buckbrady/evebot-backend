# Generated by Django 4.2.4 on 2023-08-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0002_universe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ancestry",
            name="icon_id",
            field=models.IntegerField(null=True),
        ),
    ]
