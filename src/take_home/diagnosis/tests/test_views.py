import json
from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from ..models import DiagnosisCode
from ..serializers import DiagnosisCodeSerializer

#initialize the APIClient
client = Client()

class GetDiagnosisCodesTest(TestCase):
    """ Test module for GET all diagnoisis codes API """

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

    def test_get_diagnosis_codes(self):
        # get API response
        response = client.get(reverse('get_post_diagnosis_codes'))
        # get data from db
        diagnosis_codes = DiagnosisCode.objects.all()[:20]
        serializer = DiagnosisCodeSerializer(diagnosis_codes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleDiagnosisCodeTest(TestCase):
    """ Test module for GET single diagnoisis code API """

    def setUp(self):
        self.diagnosis_code_a009 = DiagnosisCode.objects.create(
            category_code = 'A00',
            diagnosis_code = '9',
            full_code = 'A009',
            abbreviated_desc = 'Cholera, unspecified',
            full_desc = 'Cholera, unspecified',
            category_title = 'Cholera',
            icd_version = 'icd-9'
        )

        self.diagnosis_code_a038 = DiagnosisCode.objects.create(
            category_code = 'A03',
            diagnosis_code = '8',
            full_code = 'A038',
            abbreviated_desc = 'Other shigellosis',
            full_desc = 'Other shigellosis',
            category_title = 'shigellosis',
            icd_version = 'icd-10'
        )

    def test_get_valid_single_diagnosis_code(self):
        response = client.get(
            reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.diagnosis_code_a009.pk}))
        diagnosis_code = DiagnosisCode.objects.get(pk=self.diagnosis_code_a009.pk)
        serializer = DiagnosisCodeSerializer(diagnosis_code)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_diagnosis_code(self):
        response = client.get(
            reverse('get_delete_update_diagnosis_code', kwargs={'pk': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewDiagnosisCodeTest(TestCase):
    """ Test module for inserting a new diagnoisis code """

    def setUp(self):
        self.valid_payload = {
            'category_code': 'A00',
            'diagnosis_code': '9',
            'full_code': 'A009',
            'abbreviated_desc': 'Cholera, unspecified',
            'full_desc': 'Cholera, unspecified',
            'category_title': 'Cholera',
            'icd_version': 'icd-9'
        }

        self.invalid_payload = {
            'category_code': '',
            'diagnosis_code': '9',
            'full_code': '',
            'abbreviated_desc': 'Cholera, unspecified',
            'full_desc': 'Cholera, unspecified',
            'category_title': 'Cholera',
            'icd_version': 'icd-9'
        }

    def test_create_valid_diagnosis_code(self):
        response = client.post(
            reverse('get_post_diagnosis_codes'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_diagnosis_code(self):
        response = client.post(
            reverse('get_post_diagnosis_codes'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleDiagnosisCodeTest(TestCase):
    """ Test module for updating an existing diagnoisis code record """

    def setUp(self):
        self.diagnosis_code_a009 = DiagnosisCode.objects.create(
            category_code = 'A00',
            diagnosis_code = '9',
            full_code = 'A009',
            abbreviated_desc = 'Cholera, unspecified',
            full_desc = 'Cholera, unspecified',
            category_title = 'Cholera',
            icd_version = 'icd-9'
        )

        self.diagnosis_code_a038 = DiagnosisCode.objects.create(
            category_code = 'A03',
            diagnosis_code = '8',
            full_code = 'A038',
            abbreviated_desc = 'Other shigellosis',
            full_desc = 'Other shigellosis',
            category_title = 'shigellosis',
            icd_version = 'icd-10'
        )
        self.valid_payload = {
            'category_code': 'A00',
            'diagnosis_code': '9',
            'full_code': 'A009',
            'abbreviated_desc': 'Cholera, unspecified',
            'full_desc':'Cholera, unspecified',
            'category_title': 'Cholera',
            'icd_version': 'icd-9'
        }

        self.invalid_payload = {
            'category_code': '',
            'diagnosis_code': '9',
            'full_code': '',
            'abbreviated_desc': 'Cholera, unspecified',
            'full_desc': 'Cholera, unspecified',
            'category_title': 'Cholera',
            'icd_version':'icd-9'
        }

    def test_valid_update_diagnosis_code(self):
        response = client.put(
            reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.diagnosis_code_a009.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_diagnosis_code(self):
        response = client.put(
            reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.diagnosis_code_a009.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleDiagnosisCodeTest(TestCase):
    """ Test module for GET single diagnoisis code API """

    def setUp(self):
        self.diagnosis_code_a009 = DiagnosisCode.objects.create(
            category_code = 'A00',
            diagnosis_code = '9',
            full_code = 'A009',
            abbreviated_desc = 'Cholera, unspecified',
            full_desc = 'Cholera, unspecified',
            category_title = 'Cholera',
            icd_version = 'icd-9'
        )

        self.diagnosis_code_a038 = DiagnosisCode.objects.create(
            category_code = 'A03',
            diagnosis_code = '8',
            full_code = 'A038',
            abbreviated_desc = 'Other shigellosis',
            full_desc = 'Other shigellosis',
            category_title = 'shigellosis',
            icd_version = 'icd-10'
        )

    def test_delete_valid_single_diagnosis_code(self):
        response = client.delete(
            reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.diagnosis_code_a009.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_diagnosis_code(self):
        response = client.delete(
            reverse('get_delete_update_diagnosis_code', kwargs={'pk': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)