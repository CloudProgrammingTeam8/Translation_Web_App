from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Record(models.Model):
    words = models.TextField()
    user = models.TextField()
    time = models.DateField(blank=True, null=True)
    word_count = models.IntegerField()

class S3store(models.Model):
    record_id = models.TextField()
    url = models.TextField()

class Translatioin(models.Model):
    record_id = models.TextField()
    result = models.TextField()