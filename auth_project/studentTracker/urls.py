from django.urls import path
from . import views
from .views import smart_scheduler, delete_class_schedule, delete_assignment, update_assignment_status,add_reminder



urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_confirm_view, name='logout_confirm'),
    path('logout/confirm/', views.logout_view, name='logout'),
    path('smart-scheduler/', views.smart_scheduler, name='smart_scheduler'),
    path('reminders-notifications/', views.reminders_notifications, name='reminders_notifications'),
    path('progress-tracking/', views.progress_tracking, name='progress_tracking'),
    path('wellness-checkins/', views.wellness_checkins, name='wellness_checkins'),
    path('add_class_schedule/', views.add_class_schedule, name='add_class_schedule'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('delete-class/<int:schedule_id>/', delete_class_schedule, name='delete_class_schedule'),
    path('delete-assignment/<int:assignment_id>/', delete_assignment, name='delete_assignment'),
    path('update-assignment/<int:assignment_id>/', update_assignment_status, name='update_assignment_status'),
    path('add-reminder/', add_reminder, name='add_reminder')

]

