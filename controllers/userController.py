from typing import List

from entities.user import User
from entities.session import Session
from utils import check_login, ensure_single_session


class UserController:
    users: List[User]

    def __init__(self):
        self.users = []

    def create_user(self, name: str, password: str, email: str):
        if self.find_user(email):
            print("User already exists.")
            return None
        else:
            new_user = User(name, password, email)
            self.users.append(new_user)
            return new_user

    def find_user(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
        print(f"User with email address {email} not found.")

    def find_user_by_id(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:

                return user
        print(f"User with id {user_id} not found.")

    @ensure_single_session
    def login(self, email: str, password: str):
        user = self.find_user(email)
        if user is None:
            return
        elif user.password != password:
            print("Invalid password.")
        elif user.password == password:
            print(email,password)
            user.logged_in = True
            session = Session()
            session.start_session(user.user_id)
            return user

    def show_all_users(self):
        return self.users

    def show_session(self):
        return Session().user_id

    @check_login
    def logout(self):
        session = Session()
        user = self.find_user_by_id(session.user_id)
        user.logged_in = False
        session.end_session()
        return user

    @check_login
    def get_current_user(self):
        session = Session()
        user = self.find_user_by_id(session.user_id)
        return user

    @check_login
    def follow_user(self, user_id: int):
        followuser = self.find_user_by_id(user_id)
        if followuser is None:
            print("User not found.")
            return None
        else:
            session = Session()
            user = self.find_user_by_id(session.user_id)
            followuser.followers.add(user.user_id)
            user.following.add(followuser.user_id)
            return followuser

    @check_login
    def unfollow_user(self, user_id: int):
        unfollowuser = self.find_user_by_id(user_id)
        if unfollowuser is None:
            print("User not found.")
            return None
        else:
            session = Session()
            user = self.find_user_by_id(session.user_id)
            unfollowuser.unfollow(user.user_id)
            user.following.remove(unfollowuser.user_id)
            return unfollowuser
