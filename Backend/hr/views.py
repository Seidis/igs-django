import requests
from rest_framework import viewsets, generics
from django.shortcuts import render


from hr.models import Employee, Department

from hr.serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    EmployeeDepartmentSerializer,
)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ["name", "email", "department__name"]
    ordering_fields = ["id", "name", "email", "department__name"]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeDepartmentViewSet(generics.ListAPIView):
    def get_queryset(self):
        return Employee.objects.filter(department=self.kwargs["department_id"])

    serializer_class = EmployeeDepartmentSerializer


def index(request):
    url = "http://localhost:8000/api/employees/?"

    if "search" in request.GET:
        search = request.GET["search"]
        if search:
            url += "search=" + search

    if "sort" in request.GET:
        sort = request.GET["sort"]
        if sort:
            url += "&ordering=" + sort
    else:
        url += "&ordering=id"

    if "page" in request.GET:
        page = request.GET["page"]
        if page:
            url += "&page=" + page

    response = requests.get(url)
    response_json = response.json()

    total_pages = response_json["count"] // 10
    page_number = 1
    if response_json["next"]:
        page_number = int(response_json["next"].split("page=")[1]) - 1
    if response_json["previous"] and not response_json["next"]:
        page_number = int(response_json["previous"].split("page=")[1]) + 1

    response_json["page_number"] = page_number
    response_json["total_pages"] = total_pages

    return render(
        request,
        "hr/employees_table.html",
        {"employees": response_json},
    )
