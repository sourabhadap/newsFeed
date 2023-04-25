class UserNotFoundException(Exception):
    """Exception raised when a user is not found."""
    def __init__(self, user_id):
        self.user_id = user_id
        self.message = f"User with ID {user_id} not found."
        super().__init__(self.message)


class SessionExpiredException(Exception):
    """Exception raised when a session has expired."""
    def __init__(self, session_id):
        self.session_id = session_id
        self.message = f"Session with ID {session_id} has expired."
        super().__init__(self.message)


class FeedItemNotFoundException(Exception):
    """Exception raised when a feed item is not found."""
    def __init__(self, feed_item_id):
        self.feed_item_id = feed_item_id
        self.message = f"Feed item with ID {feed_item_id} not found."
        super().__init__(self.message)


class CommentNotFoundException(Exception):
    """Exception raised when a comment is not found."""
    def __init__(self, comment_id):
        self.comment_id = comment_id
        self.message = f"Comment with ID {comment_id} not found."
        super().__init__(self.message)


class UserAlreadyExistsException(Exception):
    """Exception raised when a user already exists."""
    def __init__(self, username):
        self.username = username
        self.message = f"User with username '{username}' already exists."
        super().__init__(self.message)


class InvalidCredentialsException(Exception):
    """Exception raised when invalid credentials are provided."""
    def __init__(self, username):
        self.username = username
        self.message = f"Invalid credentials for user '{username}'."
        super().__init__(self.message)


class NotAuthorizedException(Exception):
    """Exception raised when a user is not authorized to perform an action."""
    def __init__(self, user_id):
        self.user_id = user_id
        self.message = f"User with ID {user_id} is not authorized to perform this action."
        super().__init__(self.message)


class FeedItemNotAllowedException(Exception):
    """Exception raised when a user is not allowed to perform an action on a feed item."""
    def __init__(self, user_id, feed_item_id):
        self.user_id = user_id
        self.feed_item_id = feed_item_id
        self.message = f"User with ID {user_id} is not allowed to perform this action on feed item {feed_item_id}."
        super().__init__(self.message)


class CommentNotAllowedException(Exception):
    """Exception raised when a user is not allowed to perform an action on a comment."""
    def __init__(self, user_id, comment_id):
        self.user_id = user_id
        self.comment_id = comment_id
        self.message = f"User with ID {user_id} is not allowed to perform this action on comment {comment_id}."
        super().__init__(self.message)
