import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

import random
from faker import Faker
from hr.models import Department, Employee


def create_departments(number_of_departments):
    fake = Faker("pt_BR")

    try:
        for _ in range(number_of_departments):
            department = Department.objects.create(
                name=fake.job(),
            )
            department.save()
        print("Departments created successfully")
    except Exception as e:
        print(e)


def create_employees(number_of_employees):
    fake = Faker("pt_BR")

    if Department.objects.count() == 0:
        create_departments(10)

    try:
        for _ in range(number_of_employees):
            name = fake.name()
            email = name.lower().replace(" ", ".") + "@" + fake.free_email_domain()
            employee = Employee.objects.create(
                name=name,
                email=email,
                department=Department.objects.order_by("?").first(),
            )
            employee.save()
        print("Employees created successfully")
    except Exception as e:
        print(e)


def clear_data():
    try:
        Employee.objects.all().delete()
        Department.objects.all().delete()
        print("Data cleared successfully")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_employees(100)
    # clear_data()
