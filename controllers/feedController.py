from typing import List

from entities.comment import Comment, CommentWithReplies
from entities.feed import Feed
from entities.user import User
from controllers import FeedSortingStrategy
from utils import check_login

strategies = {
            "recent": FeedSortingStrategy.SortByDate(),
            "score": FeedSortingStrategy.SortByScore(),
            "comments": FeedSortingStrategy.SortByComments()
        }


class FeedController:
    feeds: List[Feed]

    def __init__(self):
        self.feeds = []

    def get_feed(self, feed_id: int):
        for feed in self.feeds:
            if feed_id == feed.feed_id:
                return feed
        return None

    @check_login
    def create_feed(self, user: User, content: str):
        new_feed = Feed(user, content)
        self.feeds.append(new_feed)
        return new_feed

    @check_login
    def add_comment(self, feed_id: int, user: User, content: str):
        if user not in user.followers:
            print("You cannot comment on this feed.")
            return
        else:
            feed = self.get_feed(feed_id)
            new_comment = Comment(feed_id, user.user_id, content)
            feed.comments.append(new_comment)
            return new_comment

    # @check_login
    # def reply_to_comment(self, comment_id: int, user: User, content: str):
    #     comment = self.get_comment(comment_id)
    #     new_reply_comment = CommentWithReplies(comment, user, content)
    #     comment.add_comment(new_reply_comment)
    #     return new_reply_comment

    @check_login
    def upvote(self, feed_id: int):
        feed = self.get_feed(feed_id)
        feed.upvote()

    @check_login
    def downvote(self, feed_id: int):
        feed = self.get_feed(feed_id)
        feed.downvote()

    @check_login
    def upvote_comment(self, feed_int: int, comment_id: int):
        comment = self.get_feed(feed_int).get_comment(comment_id)
        comment.upvotes()

    @check_login
    def downvote_comment(self, feed_int: int, comment_id: int):
        comment = self.get_feed(feed_int).get_comment(comment_id)
        comment.downvote()

    @check_login
    def sort_feeds(self, strategy: FeedSortingStrategy):

        # if strategy == "followers":
        #     strategy = FeedSortingStrategy.SortByFollowedUsers()
        # else:
        strategy = strategies[strategy]
        strategy.sort(self.feeds)

    @check_login
    def show_feeds(self):
        for feed in self.feeds:
            feed.show_feed()
