from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)


class Clients(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    email_address = models.CharField(max_length=128)


class Defects(models.Model):
    description = models.CharField(max_length=128)
    average_price = models.IntegerField()


class Parts(models.Model):
    description = models.CharField(max_length=128)
    average_price = models.IntegerField()


class Tasks(models.Model):
    employee_receiving = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='receiving_employee')
    employee_service = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='servicing_employee')
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    bicycle_name = models.CharField(max_length=128)
    bicycle_year = models.IntegerField()
    defects = models.ManyToManyField(Defects)
    parts = models.ManyToManyField(Parts)
    priority = models.BooleanField()
    estimated_time = models.DurationField()
    notes = models.TextField()
    expected_price = models.IntegerField()
    photo = models.ImageField()
    payment_in_advance = models.IntegerField()
    reclamation = models.BooleanField()
