from abc import ABC, abstractmethod
from typing import List

from entities.feed import Feed
from entities.user import User
from entities.votes import Votes



class CommentComponent(ABC):

    @abstractmethod
    def add_comment(self, comment):
        pass

    @abstractmethod
    def display_comments(self):
        pass


# Leaf class representing a Comment
class Comment(CommentComponent, Votes):
    user_id: int
    content: str
    comment_id: int
    feed_id: int
    comment_id = 1

    def __init__(self, feed_id: int, user_id: int, content: str):
        super().__init__()
        self.comment_id = self.comment_id
        self.user_id = user_id
        self.feed_id = feed_id
        self.content = content
        self.comment_id += 1

    def add_comment(self, comment):
        # Leaf node cannot have comments
        print("Cannot add comment to a leaf node")

    def display_comments(self):
        # Leaf node has no comments to display
        print("No comments to display")


# Composite class representing a Comment with Replies
class CommentWithReplies(CommentComponent, Votes):
    comment_reply_id: int
    comment_id: int
    user_id: int
    content: str
    replies: List
    comment_reply_id = 1

    def __init__(self, comment_id, user_id, content):
        super().__init__()
        self.comment_reply_id = self.comment_reply_id
        self.comment_id = comment_id
        self.user_id = user_id
        self.content = content
        self.replies = []
        self.comment_reply_id += 1

    def add_comment(self, comment: Comment):
        # Add a reply to the list of replies
        self.replies.append(comment)

    def display_comments(self):
        print("Comment ID: ", self.comment_id)
        print("User ID: ", self.user_id)
        print("Content: ", self.content)
        print("Replies: ")
        for reply in self.replies:
            print("Reply ID: ", reply.comment_reply_id)
            print("User ID: ", reply.user_id)
            print("Content: ", reply.content)
