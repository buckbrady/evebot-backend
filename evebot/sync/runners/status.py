import logging
from sync.provider import esi
from models.models import Status

logger = logging.getLogger("sync.runners.status")


def run_server_status():
    """
    Get server status from ESI
    :return:
    """
    logger.info("Getting server status from ESI")
    res = esi.client.Status.get_status().results()
    Status.objects.create(
        server_version=res["server_version"],
        server_start_time=res["start_time"],
        players_online=res["players"],
    )
    logger.info("Finished server status sync")
