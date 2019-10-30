from django.db import models
from datetime import datetime



class Job(models.Model):
    jtitle = models.CharField(max_length=255)
    jcompany = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    jtype = models.CharField(max_length=255)
    jpost_url = models.CharField(max_length=255)
    jcompany_url = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s %s' % (self.jtitle, self.jcompany)