class Movie:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("title must be a non-empty string")
        self._title = title
        self._reviews = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception("title must be a non-empty string")

    @property
    def reviews(self):
        from review import Review
        return self._reviews

    @property
    def reviewers(self):
        from review import Review
        return list(set([review.viewer for review in self._reviews]))

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
