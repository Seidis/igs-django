from django.urls import path, include
from rest_framework import routers

from hr.views import (
    EmployeeViewSet,
    DepartmentViewSet,
    EmployeeDepartmentViewSet,
    index,
    employee,
)

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"departments", DepartmentViewSet, basename="department")

urlpatterns = [
    path("", index, name="base"),
    path("employees/<int:employee_id>/", employee, name="employee"),
    path("api/", include(router.urls)),
    path(
        "api/departments/<int:department_id>/employees/",
        EmployeeDepartmentViewSet.as_view(),
    ),
]
