from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "department"
