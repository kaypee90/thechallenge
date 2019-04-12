from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/diagnosis/(?P<pk>[0-9]+)$',
        views.get_delete_update_diagnosis_code,
        name='get_delete_update_diagnosis_code'
    ),
    url(
        r'^api/v1/diagnosis/$',
        views.get_post_diagnosis_codes,
        name='get_post_diagnosis_codes'
    )
]