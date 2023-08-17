import logging

from models.models import Category
from sync.provider import esi

logger = logging.getLogger("sync.runners.universe.category")


def run_universe_category():
    logger.info("Getting universe category from ESI")
    res = esi.client.Universe.get_universe_categories().results()
    for category in res:
        Category.objects.update_or_create(
            category_id=category["category_id"],
            defaults={
                "name": category["name"],
                "published": category["published"],
                "groups": category["groups"],
            },
        )
    logger.info("Finished universe category sync")
