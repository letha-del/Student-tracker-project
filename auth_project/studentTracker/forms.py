from django import forms
from .models import ClassSchedule, Assignment

# ClassSchedule form
class ClassScheduleForm(forms.ModelForm):
    class_name = forms.CharField(max_length=100)
    days = forms.CharField(max_length=100)
    time = forms.CharField(max_length=100)
    
    class Meta:
        model = ClassSchedule
        fields = ['class_name', 'days', 'time']

# Assignment form
class AssignmentForm(forms.ModelForm):
    assignment_name = forms.CharField(max_length=100)
    due_date = forms.DateField()
    category = forms.CharField(max_length=100)
    
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'due_date', 'category']
