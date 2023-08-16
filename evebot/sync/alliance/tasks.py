from celery import shared_task


@shared_task
def sync_alliance():
    """
    Sync alliance data from ESI
    :return:
    """
    pass


@shared_task
def sync_alliance_corporations():
    """
    Sync alliance corporations data from ESI
    :return:
    """
    pass


@shared_task
def sync_alliance_icons():
    """
    Sync alliance icons from ESI
    :return:
    """
    pass
