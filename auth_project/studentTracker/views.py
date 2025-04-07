from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ClassSchedule, Assignment
from .forms import ClassScheduleForm, AssignmentForm
import json




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

@login_required
def smart_scheduler(request):
    class_schedules = ClassSchedule.objects.all()
    assignments = Assignment.objects.all()
    
    form_class_schedule = ClassScheduleForm()
    form_assignment = AssignmentForm()

    return render(request, 'smart_scheduler.html', {
        'class_schedules': class_schedules,
        'assignments': assignments,
        'form_class_schedule': form_class_schedule,
        'form_assignment': form_assignment
    })

@login_required
def reminders_notifications(request):
    return render(request, 'reminders_notifications.html')

@login_required
def progress_tracking(request):
    return render(request, 'progress_tracking.html')

@login_required
def wellness_checkins(request):
    return render(request, 'wellness_checkins.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def logout_confirm_view(request):
    return render(request, 'logout_confirm.html')


# View to handle adding class schedule
from django.contrib import messages

@login_required
def add_class_schedule(request):
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Class has been added successfully.")
            return redirect('smart_scheduler')
    else:
        form = ClassScheduleForm()
    return render(request, 'smart_scheduler.html', {'form_class_schedule': form})


# View to handle adding assignment
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment has been added successfully.")
            return redirect('smart_scheduler')
    else:
        form = AssignmentForm()
    return render(request, 'smart_scheduler.html', {'form_assignment': form})

# View to display class schedules and assignments
def smart_scheduler(request):
    # Handle both forms in the same view
    if request.method == 'POST':
        if 'add_class' in request.POST:
            form_class_schedule = ClassScheduleForm(request.POST)
            form_assignment = AssignmentForm()
            if form_class_schedule.is_valid():
                form_class_schedule.save()

            
                return redirect('smart_scheduler')

        elif 'add_assignment' in request.POST:
            form_assignment = AssignmentForm(request.POST)
            form_class_schedule = ClassScheduleForm()
            if form_assignment.is_valid():
                form_assignment.save()
                return redirect('smart_scheduler')
    else:
        form_class_schedule = ClassScheduleForm()
        form_assignment = AssignmentForm()

    # Load all objects to display
    class_schedules = ClassSchedule.objects.all()
    assignments = Assignment.objects.all()

    return render(request, 'smart_scheduler.html', {
        'form_class_schedule': form_class_schedule,
        'form_assignment': form_assignment,
        'class_schedules': class_schedules,
        'assignments': assignments
    })

def delete_class_schedule(request, schedule_id):
    schedule = get_object_or_404(ClassSchedule, id=schedule_id)
    schedule.delete()
    return redirect('smart_scheduler')

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.delete()
    return redirect('smart_scheduler')

def update_assignment_status(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == "POST":
        # Update completion status based on checkbox input
        assignment.completed = request.POST.get("completed") == "on"
        assignment.save()
    return redirect('smart_scheduler')


from .models import Reminder  # Assuming you have a Reminder model

# This is the view function for the reminders notifications page
def reminders_notifications(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders_notifications.html', {'reminders': reminders})

def add_reminder(request):
    if request.method == 'POST':
        reminder_name = request.POST['reminder_name']
        reminder_date = request.POST['reminder_date']
        # Create and save the new reminder to the database
        Reminder.objects.create(reminder_name=reminder_name, reminder_date=reminder_date)
        return redirect('reminders_notifications')  # Redirect back to the reminders page
    return redirect('reminders_notifications')  #

