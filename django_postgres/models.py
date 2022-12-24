from django.db import models


class BenchmarkUser(models.Model):

    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False, null=True)