from django.test import TestCase
from ..models import DiagnosisCode

class DiagnosisCodeTest(TestCase):
    """ Test module for Diagnosis Code model """

    def setUp(self):
        DiagnosisCode.objects.create(
            category_code = 'A00',
            diagnosis_code = '9',
            full_code = 'A009',
            abbreviated_desc = 'Cholera, unspecified',
            full_desc = 'Cholera, unspecified',
            category_title = 'Cholera',
            icd_version = 'icd-9'
        )

        DiagnosisCode.objects.create(
            category_code = 'A03',
            diagnosis_code = '8',
            full_code = 'A038',
            abbreviated_desc = 'Other shigellosis',
            full_desc = 'Other shigellosis',
            category_title = 'shigellosis',
            icd_version = 'icd-10'
        )

    def test_diagnosis_icd_version(self):
        diagnosis_code_a009 = DiagnosisCode.objects.get(full_code='A009')
        diagnosis_code_a038 = DiagnosisCode.objects.get(full_code='A038')
        self.assertEqual(
            diagnosis_code_a009.get_icd_version(),
            "A009 belongs to icd-9 version")
        self.assertEqual(
            diagnosis_code_a038.get_icd_version(),
            "A038 belongs to icd-10 version")
