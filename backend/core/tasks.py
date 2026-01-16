from celery import shared_task

@shared_task
def notify_appointment_created(user_email, start_time, end_time):
    print(f"[Notification] User {user_email} created appointment from {start_time} to {end_time}")
