from typing import List


class User:
    name: str
    password: str
    email: str
    followers: set
    following: set
    logged_in: bool
    user_id: int
    user_count = 0

    def __init__(self, name: str, password: str, email: str):
        User.user_count += 1
        self.user_id = User.user_count
        self.name = name
        self.password = password
        self.email = email
        self.followers = set()
        self.following = set()
        self.logged_in = False

    def __repr__(self):
        return f"User :({self.user_id},{self.name}, {self.email}, {self.logged_in}, Followers :{self.followers}, " \
               f"Following :{self.following}) "

    def follow(self, user):
        if user == self:
            raise Exception("You cannot follow yourself.")
        self.followers.add(user)

    def unfollow(self, user):
        if user in self.followers:
            self.followers.remove(user)
        else:
            raise Exception("You are not following this user.")

    def get_followers(self):
        return self.followers
