from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from hr.models import Department

class DepartmentTests(APITestCase):

    def setUp(self):
        self.list_url = reverse("department-list")

        self.department_1 = Department.objects.create(name="Test Department 1")
        self.department_2 = Department.objects.create(name="Test Department 2")

    def test_get_departments(self):
        """
        Ensure we can list all departments
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Department.objects.count(), 2)

    def test_post_department(self):
        """
        Ensure we can create a new department object
        """
        data = {
            "name": "Test Department 3",
            "description": "Test Department 3 Description",
        }

        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 3)


    def test_update_department(self):
        """
        Ensure we can update a department object
        """

        data = {
            "name": "Test Department 1 Updated",
        }

        response = self.client.patch(
            reverse("department-detail", args=[self.department_1.id]), data, format="json"
        )
        response_verify = self.client.get(
            reverse("department-detail", args=[self.department_1.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_verify.data["name"], data["name"])

    def test_delete_department(self):
        """
        Ensure we can delete a department object
        """

        response = self.client.delete(
            reverse("department-detail", args=[self.department_1.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 1)