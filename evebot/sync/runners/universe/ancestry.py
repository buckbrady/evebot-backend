import logging

from models.models import Ancestry
from sync.provider import esi

logger = logging.getLogger("sync.runners.universe.ancestry")


def run_universe_ancestry():
    logger.info("Getting universe ancestry from ESI")
    res = esi.client.Universe.get_universe_ancestries().results()
    for ancestry in res:
        Ancestry.objects.update_or_create(
            ancestry_id=ancestry["id"],
            defaults={
                "name": ancestry["name"],
                "bloodline_id": ancestry["bloodline_id"],
                "description": ancestry["description"],
                "icon_id": ancestry["icon_id"],
                "short_description": ancestry["short_description"],
            },
        )
    logger.info("Finished universe ancestry sync")
