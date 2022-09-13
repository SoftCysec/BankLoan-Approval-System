from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from API.models import Approvals

class ApprovalsSerializer(serializers.ModelSerializer):
    class meta:
        model = Approvals
        field = '__all__'