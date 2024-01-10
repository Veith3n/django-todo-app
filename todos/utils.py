from .models import ActivityLog


def log_activity(user, action_type, details):
    ActivityLog.objects.create(user=user, action_type=action_type, details=details)
