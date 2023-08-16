from django.db import models
from .alliance import *


# Models below are either single endpoint resources such as the status endpoint or miscellaneous models that do not
# have an easy to place home.
class Status(models.Model):
    server_version = models.CharField(max_length=20)
    server_start_time = models.DateTimeField()
    players_online = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Status"
        db_table = "status"
