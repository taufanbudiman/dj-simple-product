from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import pagination
from rest_framework.response import Response


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, null=True)


# TODO remove if no use
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'data': data
        })
