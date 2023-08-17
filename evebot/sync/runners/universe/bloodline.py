import logging

from models.models import Bloodline
from sync.provider import esi

logger = logging.getLogger("sync.runners.universe.bloodline")


def run_universe_bloodline():
    logger.info("Getting universe bloodline from ESI")
    res = esi.client.Universe.get_universe_bloodlines().results()
    for bloodline in res:
        Bloodline.objects.update_or_create(
            ancestry_id=bloodline["bloodline_id"],
            defaults={
                "name": bloodline["name"],
                "description": bloodline["description"],
                "corporation_id": bloodline["corporation_id"],
                "race_id": bloodline["race_id"],
                "ship_type_id": bloodline["ship_type_id"],
                "perception": bloodline["perception"],
                "willpower": bloodline["willpower"],
                "charisma": bloodline["charisma"],
                "memory": bloodline["memory"],
                "intelligence": bloodline["intelligence"],
            },
        )
