from entities.session import Session
import datetime

from entities.user import User


def check_login(func):
    def wrapper(self, *args, **kwargs):
        if Session().user_id is not None:
            return func(self, *args, **kwargs)
        else:
            print("You need to log in first.")

    return wrapper


def ensure_single_session(func):
    def wrapper(*args, **kwargs):
        if Session()._instance is not None and Session()._instance.user_id is not None:
            print("Session already active for another user.")
        else:
            return func(*args, **kwargs)
    return wrapper


class TimeAgo:
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def time_ago(self):
        current_time = datetime.datetime.now()
        time_difference = current_time - self.timestamp

        if time_difference.total_seconds() < 60:
            return f"{int(time_difference.total_seconds())}s ago"
        elif time_difference.total_seconds() < 3600:
            minutes = int(time_difference.total_seconds() / 60)
            return f"{minutes}m ago"
        elif time_difference.total_seconds() < 86400:
            hours = int(time_difference.total_seconds() / 3600)
            return f"{hours}hr ago"
        else:
            days = int(time_difference.total_seconds() / 86400)
            return f"{days}d ago"