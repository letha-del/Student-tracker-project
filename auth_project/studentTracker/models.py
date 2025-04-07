from django.db import models
from django.contrib.auth.models import User

# Model for ClassSchedule
class ClassSchedule(models.Model):
    class_name = models.CharField(max_length=100)
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name

# Model for Assignment
class Assignment(models.Model):
    assignment_name = models.CharField(max_length=100)
    due_date = models.DateField()
    category = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.assignment_name
    




class Reminder(models.Model):
    reminder_name = models.CharField(max_length=200)  # Corrected the attribute name
    reminder_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.reminder_name


