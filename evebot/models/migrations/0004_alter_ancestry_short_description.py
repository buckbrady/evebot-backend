# Generated by Django 4.2.4 on 2023-08-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0003_alter_ancestry_icon_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ancestry",
            name="short_description",
            field=models.TextField(null=True),
        ),
    ]