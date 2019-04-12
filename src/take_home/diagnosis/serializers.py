from rest_framework import serializers
from .models import DiagnosisCode


class DiagnosisCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisCode
        fields = ('category_code',
            'diagnosis_code',
            'full_code',
            'abbreviated_desc',
            'full_desc',
            'category_title',
            'icd_version',
            'created_at',
            'updated_at')