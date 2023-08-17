# Generated by Django 4.2.4 on 2023-08-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ancestry",
            fields=[
                ("ancestry_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("bloodline_id", models.IntegerField()),
                ("description", models.TextField()),
                ("short_description", models.TextField()),
                ("icon_id", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Ancestries",
                "db_table": "universe_ancestry",
            },
        ),
        migrations.CreateModel(
            name="AsteroidBelt",
            fields=[
                (
                    "asteroid_belt_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.TextField()),
                ("system_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Asteroid Belts",
                "db_table": "universe_asteroid_belt",
            },
        ),
        migrations.CreateModel(
            name="Bloodline",
            fields=[
                (
                    "bloodline_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("corporation_id", models.IntegerField()),
                ("race_id", models.IntegerField()),
                ("ship_type_id", models.IntegerField()),
                ("perception", models.IntegerField()),
                ("willpower", models.IntegerField()),
                ("charisma", models.IntegerField()),
                ("memory", models.IntegerField()),
                ("intelligence", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Bloodlines",
                "db_table": "universe_bloodline",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("published", models.BooleanField()),
                ("groups", models.JSONField()),
            ],
            options={
                "verbose_name_plural": "Categories",
                "db_table": "universe_category",
            },
        ),
        migrations.CreateModel(
            name="Constellation",
            fields=[
                (
                    "constellation_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.TextField()),
                ("region_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Constellations",
                "db_table": "universe_constellation",
            },
        ),
        migrations.CreateModel(
            name="Faction",
            fields=[
                ("faction_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("corporation_id", models.IntegerField()),
                ("solar_system_id", models.IntegerField()),
                ("militia_corporation_id", models.IntegerField()),
                ("size_factor", models.FloatField()),
                ("station_count", models.IntegerField()),
                ("station_system_count", models.IntegerField()),
                ("is_unique", models.BooleanField()),
                ("icon_id", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Factions",
                "db_table": "universe_faction",
            },
        ),
        migrations.CreateModel(
            name="Graphic",
            fields=[
                ("graphic_id", models.IntegerField(primary_key=True, serialize=False)),
                ("collision_file", models.TextField()),
                ("graphic_file", models.TextField()),
                ("icon_folder", models.TextField()),
                ("sof_dna", models.TextField()),
                ("sof_fation_name", models.TextField()),
                ("sof_hull_name", models.TextField()),
                ("sof_race_name", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Graphics",
                "db_table": "universe_graphic",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                ("group_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("category_id", models.IntegerField()),
                ("published", models.BooleanField()),
                ("types", models.JSONField()),
            ],
            options={
                "verbose_name_plural": "Groups",
                "db_table": "universe_group",
            },
        ),
        migrations.CreateModel(
            name="Moon",
            fields=[
                ("moon_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("system_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Moons",
                "db_table": "universe_moon",
            },
        ),
        migrations.CreateModel(
            name="Planet",
            fields=[
                ("planet_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("system_id", models.IntegerField()),
                ("type_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Planets",
                "db_table": "universe_planet",
            },
        ),
        migrations.CreateModel(
            name="Race",
            fields=[
                ("race_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("alliance_id", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Races",
                "db_table": "universe_race",
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                ("region_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Regions",
                "db_table": "universe_region",
            },
        ),
        migrations.CreateModel(
            name="Star",
            fields=[
                ("star_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("age", models.BigIntegerField()),
                ("luminosity", models.FloatField()),
                ("spectral_class", models.TextField()),
                ("temperature", models.IntegerField()),
                ("radius", models.BigIntegerField()),
                ("solar_system_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Stars",
                "db_table": "universe_star",
            },
        ),
        migrations.CreateModel(
            name="Stargate",
            fields=[
                ("stargate_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("system_id", models.IntegerField()),
                ("type_id", models.IntegerField()),
                ("destination_stargate_id", models.IntegerField()),
                ("destination_system_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Stargates",
                "db_table": "universe_stargate",
            },
        ),
        migrations.CreateModel(
            name="Station",
            fields=[
                ("station_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("owner", models.IntegerField()),
                ("system_id", models.IntegerField()),
                ("type_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
                ("reprocessing_efficiency", models.FloatField()),
                ("reprocessing_stations_take", models.FloatField()),
                ("max_dockable_ship_volume", models.FloatField()),
                ("office_rental_cost", models.FloatField()),
                ("services", models.JSONField()),
            ],
            options={
                "verbose_name_plural": "Stations",
                "db_table": "universe_station",
            },
        ),
        migrations.CreateModel(
            name="Structure",
            fields=[
                (
                    "structure_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.TextField()),
                ("owner_id", models.IntegerField()),
                ("solar_system_id", models.IntegerField()),
                ("type_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Structures",
                "db_table": "universe_structure",
            },
        ),
        migrations.CreateModel(
            name="System",
            fields=[
                ("system_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("constellation_id", models.IntegerField()),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                ("position_z", models.FloatField()),
                ("security_class", models.TextField(null=True)),
                ("security_status", models.FloatField()),
                ("star_id", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Systems",
                "db_table": "universe_system",
            },
        ),
        migrations.CreateModel(
            name="SystemJump",
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
                ("system_id", models.IntegerField()),
                ("ship_jumps", models.IntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "System Jumps",
                "db_table": "universe_system_jump",
            },
        ),
        migrations.CreateModel(
            name="SystemKill",
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
                ("system_id", models.IntegerField()),
                ("ship_kills", models.IntegerField()),
                ("npc_kills", models.IntegerField()),
                ("pod_kills", models.IntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "System Kills",
                "db_table": "universe_system_kill",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                ("type_id", models.IntegerField(primary_key=True, serialize=False)),
                ("capacity", models.FloatField(null=True)),
                ("description", models.TextField()),
                ("graphic_id", models.IntegerField(null=True)),
                ("group_id", models.IntegerField()),
                ("icon_id", models.IntegerField(null=True)),
                ("market_group_id", models.IntegerField(null=True)),
                ("mass", models.FloatField(null=True)),
                ("name", models.TextField()),
                ("packaged_volume", models.FloatField(null=True)),
                ("portion_size", models.IntegerField(null=True)),
                ("published", models.BooleanField()),
                ("radius", models.FloatField(null=True)),
                ("volume", models.FloatField(null=True)),
            ],
            options={
                "verbose_name_plural": "Types",
                "db_table": "universe_type",
            },
        ),
        migrations.CreateModel(
            name="TypeDogmaAttribute",
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
                ("type_id", models.IntegerField()),
                ("attribute_id", models.IntegerField()),
                ("value", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Types Dogma Attributes",
                "db_table": "universe_types_dogma_attribute",
            },
        ),
        migrations.CreateModel(
            name="TypeDogmaEffect",
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
                ("type_id", models.IntegerField()),
                ("effect_id", models.IntegerField()),
                ("is_default", models.BooleanField()),
            ],
            options={
                "verbose_name_plural": "Types Dogma Effects",
                "db_table": "universe_types_dogma_effect",
            },
        ),
        migrations.AddConstraint(
            model_name="typedogmaeffect",
            constraint=models.UniqueConstraint(
                fields=("type_id", "effect_id"), name="unique_type_dogma_effect"
            ),
        ),
        migrations.AddConstraint(
            model_name="typedogmaattribute",
            constraint=models.UniqueConstraint(
                fields=("type_id", "attribute_id"), name="unique_type_dogma_attribute"
            ),
        ),
    ]
