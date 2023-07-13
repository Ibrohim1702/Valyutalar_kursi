from django.db import models


class Log(models.Model):
    Log = models.JSONField(default={'step': 0})
