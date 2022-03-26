from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'employeeId', 'department1', 'department2', 'employeeClass', 'name', 'name_kana', 'mailAddress', 'position', 'joiningDate', 'retirementDate', 'suspensionDate', 'secondedDate', 'secondedDestination', 'maidenName', 'remarks', 'status')
        