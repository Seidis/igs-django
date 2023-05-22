from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from hr.models import Employee, Department

class EmployeeTests(APITestCase):
    
    def setUp(self):
        self.list_url = reverse("employee-list")

        self.department_1 = Department.objects.create(name="Test Department 1")
        self.department_2 = Department.objects.create(name="Test Department 2")
        self.employee_1 = Employee.objects.create(
            name="Test Employee 1",
            email="test1@org.com.br",
            department=self.department_1
        )
        self.employee_2 = Employee.objects.create(
            name="Test Employee 2",
            email="test2@org.com.br",
            department=self.department_1
        )
        self.employee_3 = Employee.objects.create(
            name="Test Employee 3",
            email="test3@org.com.br",
            department=self.department_2
        )
        

    def test_get_employees(self):
        """
        Ensure we can list all employees
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 3)


    def test_update_employee(self):
        """
        Ensure we can update an employee object
        """
        data = {
            "name": "Test Employee 1 Updated",
        }

        response = self.client.patch(
            reverse("employee-detail", args=[self.employee_1.id]), data, format="json"
        )
        response_verify = self.client.get(
            reverse("employee-detail", args=[self.employee_1.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_verify.data["name"], data["name"])


    def test_post_employee(self):
        """
        Ensure we can create a new employee object
        """

        data = {
            "name": "Test Employee 4",
            "email": "test4@org.com.br",
            "department": self.department_1.id
        }

        response = self.client.post(self.list_url, data, format="json")
        response_verify = self.client.get(
            reverse("employee-detail", args=[response.data["id"]])
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 4)


    def test_delete_employee(self):
        """
        Ensure we can delete an employee object
        """

        response = self.client.delete(
            reverse("employee-detail", args=[self.employee_1.id])
        )
        response_verify = self.client.get(
            reverse("employee-detail", args=[self.employee_1.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 2)