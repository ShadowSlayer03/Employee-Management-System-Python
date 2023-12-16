from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name # Return a human-readable representation of the model

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name # Return a human-readable representation of the model

class Employee(models.Model):
    # Define your fields here
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name # Return a human-readable representation of the model