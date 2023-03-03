from viewer import Viewer
from movie import Movie

class Review:
    def __init__(self, viewer, movie, rating):
        if not isinstance(viewer, Viewer):
            raise Exception("viewer must be an instance of the Viewer class")
        if not isinstance(movie, Movie):
            raise Exception("movie must be an instance of the Movie class")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise Exception("rating must be an integer between 1 and 5")
        self._viewer = viewer
        self._movie = movie
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            raise Exception("rating must be an integer between 1 and 5")

    @property
    def viewer(self):
        return self._viewer

    @property
    def movie(self):
        return self._movie