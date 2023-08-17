from django.db import models


class Type(models.Model):
    """
    Universe Types endpoint model
    """

    class Meta:
        verbose_name_plural = "Types"
        db_table = "universe_type"

    type_id = models.IntegerField(primary_key=True)
    capacity = models.FloatField(null=True)
    description = models.TextField()
    graphic_id = models.IntegerField(null=True)
    group_id = models.IntegerField()
    icon_id = models.IntegerField(null=True)
    market_group_id = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    name = models.TextField()
    packaged_volume = models.FloatField(null=True)
    portion_size = models.IntegerField(null=True)
    published = models.BooleanField()
    radius = models.FloatField(null=True)
    volume = models.FloatField(null=True)


class TypeDogmaAttribute(models.Model):
    """
    Universe Types Dogma Attributes
    """

    class Meta:
        verbose_name_plural = "Types Dogma Attributes"
        db_table = "universe_types_dogma_attribute"
        constraints = [
            models.UniqueConstraint(
                fields=["type_id", "attribute_id"], name="unique_type_dogma_attribute"
            )
        ]

    type_id = models.IntegerField()
    attribute_id = models.IntegerField()
    value = models.FloatField()


class TypeDogmaEffect(models.Model):
    """
    Universe Types Dogma Effects
    """

    class Meta:
        verbose_name_plural = "Types Dogma Effects"
        db_table = "universe_types_dogma_effect"
        constraints = [
            models.UniqueConstraint(
                fields=["type_id", "effect_id"], name="unique_type_dogma_effect"
            )
        ]

    type_id = models.IntegerField()
    effect_id = models.IntegerField()
    is_default = models.BooleanField()
