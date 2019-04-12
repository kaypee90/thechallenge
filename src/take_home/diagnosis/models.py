# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DiagnosisCode(models.Model):
    """
    Diagnosis Code Model
    Defines the attributes of a diagnosis code
    """

    category_code = models.CharField(max_length=10)
    diagnosis_code = models.CharField(max_length=10, null=True, blank=True)
    full_code = models.CharField(max_length=50)
    abbreviated_desc = models.CharField(max_length=125)
    full_desc = models.CharField(max_length=255)
    category_title = models.CharField(max_length=125)
    icd_version = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_icd_version(self):
        return "{} belongs to {} version".format(self.full_code, self.icd_version)

    