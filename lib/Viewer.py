class Viewer:
    used_usernames = set()

    def __init__(self, username):
        if not isinstance(username, str) or len(username) < 6 or len(username) > 16:
            raise Exception("username must be a string between 6 and 16 characters")
        if username in Viewer.used_usernames:
            raise Exception("username must be unique")
        self._username = username
        Viewer.used_usernames.add(username)
        self._reviews = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 6 <= len(new_username) <= 16:
            if new_username not in Viewer.used_usernames:
                Viewer.used_usernames.remove(self._username)
                self._username = new_username
                Viewer.used_usernames.add(new_username)
            else:
                raise Exception("username must be unique")
        else:
            raise Exception("username must be a string between 6 and 16 characters")

    @property
    def reviews(self):
        from review import Review
        return self._reviews

    @property
    def reviewed_movies(self):
        from review import Review
        return list(set([review.movie for review in self._reviews]))

    def reviewed_movie(self, movie):
        print(f"reviewed_movies: {self.reviewed_movies}")
        print(f"movie: {movie}")
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        pass