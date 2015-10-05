
from modules.entity.movie import Movie

class MovieHandler(object):
    '''
    This class manage the movie objects and acts as interface between MovieView and Movie classes.
    '''
    
    def register_movie(self, movie_data):
        '''
        This method create a Movie object based on data sent as parameter and save it.
        '''
        new_movie = Movie()
        new_movie.load_data(movie_data)
        new_movie.save()
    