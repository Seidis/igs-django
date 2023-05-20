from django.urls import path, include
from rest_framework import routers

from hr.views import EmployeeViewSet, DepartmentViewSet, EmployeeDepartmentViewSet

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"departments", DepartmentViewSet, basename="department")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "departments/<int:department_id>/employees/",
        EmployeeDepartmentViewSet.as_view(),
    ),
]
