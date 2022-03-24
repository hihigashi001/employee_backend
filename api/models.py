from django.db import models


class Employee(models.Model):

    employeeId = models.CharField(max_length=50)
    department1 = models.CharField(max_length=50, blank=True, null=True)
    department2 = models.CharField(max_length=50, blank=True, null=True)
    employeeClass = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_kana = models.CharField(max_length=50, blank=True, null=True)
    mailAddress = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    joiningDate = models.CharField(max_length=50, blank=True, null=True)
    retirementDate = models.CharField(max_length=50, blank=True, null=True)
    suspensionDate = models.CharField(max_length=50, blank=True, null=True)
    secondedDate = models.CharField(max_length=50, blank=True, null=True)
    secondedDestination = models.CharField(max_length=50, blank=True, null=True)
    maidenName = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.employeeId