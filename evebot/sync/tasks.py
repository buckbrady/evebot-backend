import logging
from celery import shared_task
from django.utils import timezone
from esi.clients import EsiClientProvider
from models.models import Status

# create your own provider
esi = EsiClientProvider()

logger = logging.getLogger(__name__)


@shared_task
def server_status():
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
