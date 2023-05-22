from django.urls import path, include
from rest_framework import routers
from django.shortcuts import redirect


from hr.views import (
    EmployeeViewSet,
    DepartmentViewSet,
    EmployeeDepartmentViewSet,
    index,
)

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"departments", DepartmentViewSet, basename="department")

urlpatterns = [
    path("", index, name="base"),
    path("api/", include(router.urls)),
    path(
        "api/departments/<int:department_id>/employees/",
        EmployeeDepartmentViewSet.as_view(),
    ),
]
