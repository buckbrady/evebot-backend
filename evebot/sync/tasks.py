import logging

from celery import shared_task

from sync.provider import esi
from sync.runners.status import run_server_status
from sync.runners.universe.ancestry import run_universe_ancestry
from sync.runners.universe.bloodline import run_universe_bloodline
from sync.runners.universe.category import run_universe_category
from sync.runners.universe.type import run_universe_type

logger = logging.getLogger("sync.tasks")


@shared_task
def status_status():
    """
    Get server status from ESI
    :return:
    """
    run_server_status()


# Universe Tasks
@shared_task
def universe_ancestry():
    """
    Get universe ancestry from ESI
    :return:
    """
    run_universe_ancestry()


@shared_task
def universe_asteroid_belt():
    """
    Get universe asteroid belt from ESI
    :return:
    """
    pass


@shared_task
def universe_bloodline():
    """
    Get universe bloodline from ESI
    :return:
    """
    run_universe_bloodline()


@shared_task
def universe_category():
    """
    Get universe category from ESI
    :return:
    """
    run_universe_category()


@shared_task
def universe_constellation():
    """
    Get universe constellation from ESI
    :return:
    """
    pass


@shared_task
def universe_faction():
    """
    Get universe faction from ESI
    :return:
    """
    pass


@shared_task
def universe_graphics():
    """
    Get universe graphics from ESI
    :return:
    """
    pass


@shared_task
def universe_group():
    """
    Get universe group from ESI
    :return:
    """
    pass


@shared_task
def universe_moon():
    """
    Get universe moon from ESI
    :return:
    """
    pass


@shared_task
def universe_planet():
    """
    Get universe planet from ESI
    :return:
    """
    pass


@shared_task
def universe_race():
    """
    Get universe races from ESI
    :return:
    """
    pass


@shared_task
def universe_region():
    """
    Get universe region from ESI
    :return:
    """
    pass


@shared_task
def universe_stargate():
    """
    Get universe stargate from ESI
    :return:
    """
    pass


@shared_task
def universe_star():
    """
    Get universe star from ESI
    :return:
    """
    pass


@shared_task
def universe_station():
    """
    Get universe station from ESI
    :return:
    """
    pass


@shared_task
def universe_structure():
    """
    Get universe structure from ESI
    :return:
    """
    pass


@shared_task
def universe_system():
    """
    Get universe system from ESI
    :return:
    """
    pass


@shared_task
def universe_system_jumps():
    """
    Get universe system jump from ESI
    :return:
    """
    pass


@shared_task
def universe_system_kills():
    """
    Get universe system kills from ESI
    :return:
    """
    pass


@shared_task
def universe_type():
    """
    Get universe type from ESI

    Gathers all available types from ESI and then runs a task for each type to get the type details
    :return:
    """
    logger.info("Getting universe type from ESI")
    res = esi.client.Universe.get_universe_types().results()
    for type_id in res:
        logger.info(f"calling universe_type_process for {type_id}")
        universe_type_process.delay(type_id)
    logger.info("Finished universe type sync")


@shared_task
def universe_type_process(type_id):
    """
    Get universe type from ESI
    :return:
    """
    run_universe_type(type_id)