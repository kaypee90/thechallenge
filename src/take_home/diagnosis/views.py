# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DiagnosisCode
from .serializers import DiagnosisCodeSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_diagnosis_code(request, pk):
    try:
        diagnosis_code = DiagnosisCode.objects.get(pk=pk)
    except DiagnosisCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # get details of a single diagnosis code
    if request.method == 'GET':
        serializer = DiagnosisCodeSerializer(diagnosis_code)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # delete a single diagnosis code
    elif request.method == 'DELETE':
        diagnosis_code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update details of a single diagnosis code    
    elif request.method == 'PUT':
        serializer = DiagnosisCodeSerializer(diagnosis_code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_diagnosis_codes(request):
    # get 20 diagnosis codes
    if request.method == 'GET':
        limit = request.query_params.get('limit', 20)
        page = request.query_params.get('page', 1)

        try:
            queryset = DiagnosisCode.objects.all()
            paginator = Paginator(queryset, limit)
            page_of_diagnosis_codes = paginator.page(page)
            serializer = DiagnosisCodeSerializer(page_of_diagnosis_codes, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except IndexError:
            return Response({'results': []}, status=status.HTTP_200_OK)
        except PageNotAnInteger:
            return Response(
                {'data': 'Please ensure `page` is an integer'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except EmptyPage:
            return Response({'data': 'Response not found'}, status=status.HTTP_404_NOT_FOUND)

    # insert a new record for a diagnosis code
    elif request.method == 'POST':
        data = {
            'category_code': request.data.get('category_code'),
            'diagnosis_code': request.data.get('diagnosis_code'),
            'full_code': request.data.get('full_code'),
            'abbreviated_desc': request.data.get('abbreviated_desc'),
            'full_desc': request.data.get('full_desc'),
            'category_title': request.data.get('category_title'),
            'icd_version': request.data.get('icd_version')
        }
        serializer = DiagnosisCodeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
