from rest_framework import serializers
from hr.models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source="department.name")

    class Meta:
        model = Employee
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeDepartmentSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source="department.name")

    class Meta:
        model = Employee
        fields = "__all__"
