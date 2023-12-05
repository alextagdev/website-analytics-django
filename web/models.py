# notes/models.py

from django.db import models

class PerformanceAnalysis(models.Model):
    url = models.URLField()
    load_time = models.FloatField(default=0.0)
    
    load_time = models.FloatField(null=True)
    request_count = models.IntegerField(null=True)
    request_count = models.IntegerField(default=0)
    file_size = models.IntegerField(null=True)
    file_size = models.IntegerField(default=0)
    server_response_time = models.FloatField(null=True)
    bytes_received = models.IntegerField(default=0)
    content_displayed = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=20)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.url} - Load Time: {self.load_time} seconds"
