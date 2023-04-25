from abc import ABC, abstractmethod

from controllers.userController import UserController
from entities.session import Session
from entities.user import User


class FeedSortingStrategy(ABC):

    @abstractmethod
    def sort(self, feeds):
        pass


class SortByFollowedUsers(FeedSortingStrategy):
    def __init__(self,followed_users):
        self.followed_users = followed_users

    def sort(self, feeds):
        followed_news_items = []
        non_followed_news_items = []
        for feed in feeds:
            if feed.user.user_id in self.followed_users:
                followed_news_items.append(feed)
            else:
                non_followed_news_items.append(feed)
        sorted_feeds = followed_news_items + non_followed_news_items
        return sorted_feeds


class SortByScore(FeedSortingStrategy):
    def sort(self, feeds):
        feeds.sort(key=lambda x: x.score, reverse=True)
        return feeds


class SortByComments(FeedSortingStrategy):
    def sort(self, feeds):
        feeds.sort(key=lambda x: len(x.comments), reverse=True)
        return feeds


class SortByDate(FeedSortingStrategy):
    def sort(self, feeds):
        feeds.sort(key=lambda x: x.date, reverse=True)
        return feeds