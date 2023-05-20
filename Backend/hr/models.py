from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

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
