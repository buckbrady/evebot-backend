import logging
from sync.provider import esi
from models.models import Type, TypeDogmaAttribute, TypeDogmaEffect

logger = logging.getLogger("sync.runners.type")


def run_universe_type(type_id: int):
    """
    Get universe type from ESI
    :param type_id:
    :return:
    """
    logger.info("Getting universe type from ESI")
    res = esi.client.Universe.get_universe_types_type_id(type_id=type_id).results()
    logger.info("Creating or updating universe type")
    Type.objects.update_or_create(
        type_id=res["type_id"],
        defaults={
            "name": res["name"],
            "description": res["description"],
            "published": res["published"],
            "group_id": res["group_id"],
            "market_group_id": res["market_group_id"],
            "icon_id": res["icon_id"],
            "capacity": res["capacity"],
            "portion_size": res["portion_size"],
            "mass": res["mass"],
            "volume": res["volume"],
            "packaged_volume": res["packaged_volume"],
            "radius": res["radius"],
            "graphic_id": res["graphic_id"],
        },
    )

    if res["dogma_attributes"] is not None:
        logger.info("Creating or updating universe type dogma attributes")
        for attribute in res["dogma_attributes"]:
            TypeDogmaAttribute.objects.update_or_create(
                type_id=res["type_id"],
                attribute_id=attribute["attribute_id"],
                defaults={"value": attribute["value"]},
            )

    if res["dogma_effects"] is not None:
        logger.info("Creating or updating universe type dogma effects")
        for effect in res["dogma_effects"]:
            TypeDogmaEffect.objects.update_or_create(
                type_id=res["type_id"],
                effect_id=effect["effect_id"],
                defaults={"is_default": effect["is_default"]},
            )

    logger.info("Finished universe type sync")
