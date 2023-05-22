import json
import requests
from rest_framework import viewsets, generics
from django.shortcuts import render
from django.db.models import Q

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


def index(request):
    response = requests.get("http://localhost:8000/api/employees/")
    employees = json.loads(response.text)

    if "search" in request.GET:
        search = request.GET["search"]
        if search:
            filtered_employees = []
            for employee in employees:
                # Excluindo o campo "id" da validação
                values = [
                    value.lower() for key, value in employee.items() if key != "id"
                ]
                if any(search.lower() in value for value in values):
                    filtered_employees.append(employee)
            employees = filtered_employees

    return render(request, "hr/employees_table.html", {"employees": employees})


def employee(request, employee_id):
    employee = requests.get(f"http://localhost:8000/api/employees/" + str(employee_id))
    return render(request, "hr/employee.html", {"employee": employee.json()})
