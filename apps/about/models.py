from django.db import models


class About(models.Model):
    user_agent = models.CharField(max_length=255)
    remote_address = models.CharField(max_length=16, null=True)
    time = models.TimeField(auto_now=True)
