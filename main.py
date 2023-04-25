from controllers import feedController
from controllers.feedController import FeedController
from controllers.userController import UserController
import inspect


class ManagerCommand:

    def __init__(self):
        usercontroller = UserController()
        feedcontroller = FeedController()
        self.usercontroller = usercontroller
        self.feedcontroller = feedcontroller

    def show_users(self):
        return self.usercontroller.show_all_users()

    def signup(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        return self.usercontroller.create_user(username, password, email)

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        self.usercontroller.login(email, password)

    def logout(self):
        self.usercontroller.logout()

    def follow_user(self):
        user_id = int(input("Enter user id: "))
        self.usercontroller.follow_user(user_id)

    def unfollow_user(self):
        user_id = int(input("Enter user id: "))
        self.usercontroller.unfollow_user(user_id)

    def create_feed(self):
        user = self.usercontroller.get_current_user()
        content = input("Enter content: ")
        self.feedcontroller.create_feed(user, content)

    def add_comment(self):
        feed_id = int(input("Enter feed id: "))
        content = input("Enter content: ")
        user = self.usercontroller.get_current_user()
        self.feedcontroller.add_comment(feed_id, user, content)

    # def reply_comment(self):
    #     comment_id = input("Enter comment id: ")
    #     content = input("Enter content: ")
    #     user = self.usercontroller.get_current_user()
    #     self.feedcontroller.reply_comment(comment_id,user,content)
    #     print("Comment replied successfully")

    def upvote_feed(self):
        feed_id = int(input("Enter feed id: "))
        self.feedcontroller.upvote(feed_id)

    def downvote_feed(self):
        feed_id = int(input("Enter feed id: "))
        self.feedcontroller.downvote(feed_id)

    def upvote_comment(self):
        feed_id = int(input("Enter feed id: "))
        comment_id = int(input("Enter comment id: "))
        self.feedcontroller.upvote_comment(feed_id, comment_id)

    def downvote_comment(self):
        feed_id = int(input("Enter feed id: "))
        comment_id = int(input("Enter comment id: "))
        self.feedcontroller.downvote_comment(feed_id, comment_id)

    def show_feeds(self):
        self.feedcontroller.show_feeds()

    def sort_feeds(self):
        sort_strategy = input("Enter sort strategy: ")
        if sort_strategy not in feedController.strategies:
            print("Invalid sort strategy.")
            return
        self.feedcontroller.sort_feeds(sort_strategy)

    def exit(self):
        pass

    def get_session(self):
        return self.usercontroller.show_session()

    def switch(self, case_value):
        return getattr(self, case_value, lambda: 'This is default case')()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manager = ManagerCommand()
    usercontroller = manager.usercontroller
    feedcontroller = manager.feedcontroller
    user1 = usercontroller.create_user("sa", "123", "sag")
    user2 = usercontroller.create_user("so", "123", "sog")
    user3 = usercontroller.create_user("su", "123", "sug")
    usercontroller.login("sag", "123")
    feed1 = feedcontroller.create_feed(user1, "Hello")
    usercontroller.follow_user(2)
    usercontroller.logout()
    usercontroller.login("sog", "123")
    feed2 = feedcontroller.create_feed(user2, "Hi")
    feed4 = feedcontroller.create_feed(user2, "Hiiiiii")
    usercontroller.follow_user(1)
    usercontroller.logout()
    usercontroller.login("sug", "123")
    feed3 = feedcontroller.create_feed(user1, "Hey")
    usercontroller.follow_user(1)
    usercontroller.logout()
    # usercontroller.login("sag", "123")
    # print("User 1 feeds")
    # feedcontroller.sort_feeds("followers")
    all_methods = dir(manager)
    methods = [m for m in all_methods if callable(getattr(manager, m)) and not m.startswith('__')]
    # print(methods)
    case = ""

    while case != "exit":
        print(methods)
        case = input("Enter command: ")
        result = manager.switch(case)
        if result is None:
            pass
        else:
            print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
