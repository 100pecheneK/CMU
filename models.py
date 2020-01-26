from django.db import models


class CMU(models.Model):
    object_url = models.CharField(max_length=400)
