from rest_framework import viewsets, generics

from hr.models import Employee, Department

from hr.serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    EmployeeDepartmentSerializer,
)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeDepartmentViewSet(generics.ListAPIView):
    def get_queryset(self):
        return Employee.objects.filter(department=self.kwargs["department_id"])

    serializer_class = EmployeeDepartmentSerializer
