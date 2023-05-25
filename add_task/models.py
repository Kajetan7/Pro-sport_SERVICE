from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Clients(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    email_address = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Defects(models.Model):
    description = models.CharField(max_length=128)
    average_price = models.IntegerField()

    def __str__(self):
        return f"{self.description} {self.average_price}"


class Parts(models.Model):
    description = models.CharField(max_length=128)
    average_price = models.IntegerField()

    def __str__(self):
        return f"{self.description} {self.average_price}"


class Tasks(models.Model):
    employee_receiving = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='receiving_employee', null=True)
    employee_service = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='servicing_employee', null=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True)
    bicycle_name = models.CharField(max_length=128, null=True)
    bicycle_year = models.IntegerField(null=True)
    defects = models.ManyToManyField(Defects, null=True, through='TasksDefects')
    parts = models.ManyToManyField(Parts, null=True, through='TasksParts')
    priority = models.BooleanField(null=True)
    estimated_time = models.DurationField(null=True)
    notes = models.TextField(null=True)
    expected_price = models.IntegerField(null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    payment_in_advance = models.IntegerField(null=True)
    reclamation = models.BooleanField(null=True)


class TasksDefects(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    defect = models.ForeignKey(Defects, on_delete=models.CASCADE)


class TasksParts(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)