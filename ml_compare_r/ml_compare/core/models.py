from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    CHOICES = [
        ('1', 'Specifications'),
        ('2', 'Requirements'),
    ]
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    doc_type = models.CharField(blank=True, choices=CHOICES, max_length=10)
