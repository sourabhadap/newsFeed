from entities.user import User


class Session:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user_id = None
        return cls._instance

    def start_session(self, user_id):
        if self.user_id is None:
            self.user_id = user_id
        else:
            raise Exception("Session already started.")

    def end_session(self):
        if self.user_id is not None:
            self.user_id = None
        else:
            raise Exception("Session already ended.")

    def check_session(self):
        if self.user_id is not None:
            return True
        else:
            return False