from django.db import models


class System(models.Model):
    """
    Universe Systems endpoint model
    """

    class Meta:
        verbose_name_plural = "Systems"
        db_table = "universe_system"

    system_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    constellation_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()
    security_class = models.TextField(null=True)
    security_status = models.FloatField()
    star_id = models.IntegerField()


class SystemJump(models.Model):
    """
    Universe System Jumps endpoint model
    """

    class Meta:
        verbose_name_plural = "System Jumps"
        db_table = "universe_system_jump"

    system_id = models.IntegerField()
    ship_jumps = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class SystemKill(models.Model):
    """
    Universe System Kills endpoint model
    """

    class Meta:
        verbose_name_plural = "System Kills"
        db_table = "universe_system_kill"

    system_id = models.IntegerField()
    ship_kills = models.IntegerField()
    npc_kills = models.IntegerField()
    pod_kills = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
