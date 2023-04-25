class Votes:
    upvotes: int
    downvotes: int

    def __init__(self):
        self.upvotes = 0
        self.downvotes = 0
        self.score = self.upvotes - self.downvotes

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1

    def get_score(self):
        return self.upvotes - self.downvotes

    def get_upvotes(self):
        return self.upvotes

    def get_downvotes(self):
        return self.downvotes

