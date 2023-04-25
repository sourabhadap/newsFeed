from datetime import datetime
from entities.user import User
from typing import List

from entities.votes import Votes
from utils import TimeAgo


class Feed(Votes):
    user: User
    content: str
    score: int
    comments : List
    created_at: datetime
    feed_id: int
    feed_count = 0

    def __init__(self, user: User, content: str):
        super().__init__()
        Feed.feed_count += 1
        self.feed_id = Feed.feed_count
        self.user = user
        self.content = content
        self.comments = []
        self.created_at = datetime.now()

    def show_feed(self):
        created_on = TimeAgo(self.created_at)
        print("Feed ID: ", self.feed_id)
        print("User ID: ", self.user.user_id)
        print("Content: ", self.content)
        print("Upvotes: ", self.upvotes)
        print("Downvotes: ", self.downvotes)
        print("Created at: ", created_on.time_ago())
        print("Comments: ", self.comments)

    def get_comment(self,comment_id: int):
        for comment in self.comments:
            if comment_id == comment.comment_id:
                return comment
        return None