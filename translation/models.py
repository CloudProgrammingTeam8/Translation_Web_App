from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Record(models.Model):
    words = models.TextField()
    user = models.TextField()
    time = models.DateField(blank=True, null=True)
    input_lan = models.TextField()

class Translatioin(models.Model):
    record_id = models.TextField()
    result = models.TextField()
    output_lan = models.TextField()
    
class S3store(models.Model):
    record_id = models.TextField()
    source_url = models.TextField()
    output_url = models.TextField()