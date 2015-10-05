
from utils.input_validation import *
from modules.handler.movie_handler import MovieHandler

class MovieView(object):
    '''
    This class is the interface to register a movie from console
    '''

    def __init__(self):
        '''
        Initialize a new MovieView object.  
        '''
        self.movie_data = {}
        self.handler = MovieHandler()

    def display_register_inputs(self):
        '''
        This method displays a console user interface to insert the movie data
        '''
        print "Insert new Movie Information"
        self.movie_data['code'] = get_required_input("Code")
        self.movie_data['title'] = get_required_input("Title")
        self.movie_data['release_year'] = get_integer_input("Release Year")
        self.movie_data['director'] = get_required_input("Director")
        self.movie_data['story_line'] = get_optional_input("Story Line")
        self.movie_data['stars'] = self.get_multiple_inputs("Actor(star)")
        self.movie_data['rating'] = get_optional_integer_input("Rating")
        self.movie_data['ranking'] = get_optional_integer_input("Ranking")
        self.movie_data['genres'] = self.get_multiple_inputs("Genre")
        self.movie_data['rental_price'] = get_optional_float_input("Rental Price")
        self.movie_data['purchase_price'] = get_optional_float_input("Purchase Price")
        self.movie_data['quantity'] = get_optional_integer_input("Quantity")
        if ask_confirmation_question("Do you want to save the movie information?") == True:
            self.handler.register_movie(self.movie_data)
        else:
            print "Registration cancelled."

    def get_multiple_inputs(self, item_name):
        '''
        Reads multiple inputs from console. Returns an Array[String] with all values inserted.
        
        Params:
        @item_name    String with the name of the item.
        '''
        values_list = []
        while True:
            value = get_optional_input(item_name)
            if not value:
                break
            else:
                values_list.append(value)
            if ask_confirmation_question("Do you want to add another " + item_name + "?") == False:
                break
        return values_list

if __name__ == '__main__':
    movie_menu = MovieView()
    movie_menu.display_register_inputs()