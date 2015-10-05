
from database.database_connection import DataBase
from modules.entity.actor import Actor
from modules.entity.genre import Genre

class Movie(object):
    '''
    This class defines a movie object.
    '''


    def __init__(self):
        '''
        Initialize a new movie object.
        
        Params:
        @movie_data    Dictionary that contains all movie data
        '''
        self.db_handler = DataBase('DB_MOVIE_RENTAL.db')
        self.table = "MOVIE"
    
    def set_title(self, new_title):
        '''
        This method sets a new movie title.
        
        Params:
        @new_title    String - The movie title that will replace the old one. 
        '''
        self.title = new_title
    
    def set_release_year(self, release_year):
        '''
        This method sets the movie's release year.
        
        Params:
        @release_year    Integer - The year when the movie was released. 
        '''
        self.release_year = release_year
    
    def set_stars(self, stars_list):
        '''
        This method sets the main actors in the movie.
        
        Params:
        @stars_list    Array[String] - A list of the main actors in the movie. 
        '''
        self.stars = stars_list
    
    def set_director(self, director_name):
        '''
        This method sets the movie's director.
        
        Params:
        @director_name    String - The name of movie's director. 
        '''
        self.director = director_name
    
    def set_genres(self, genres_list):
        '''
        This method sets the genres that the movie belongs.
        
        Params:
        @genres_list    Array[String] - A list of the genres that the movie belongs. 
        '''
        self.genres = genres_list
    
    def set_story_line(self, story_line):
        '''
        This method sets the movie story line.
        
        Params:
        @story_line    String - the movie story line. 
        '''
        self.story_line = story_line
    
    def set_rating(self, rating):
        '''
        This method sets the rating in the movie.
        
        Params:
        @rating    Integer - the rating in the movie.
        '''
        self.rating = rating
    
    def set_ranking(self, ranking):
        '''
        This method sets the ranking in the movie.
        
        Params:
        @ranking    Integer - the ranking in the movie.
        '''
        self.ranking = ranking
    
    def set_rental_price(self, rental_price):
        '''
        This method sets the rental price.
        
        Params:
        @rental_price    Float - the current rental price.
        '''
        self.rental_price = rental_price
    
    def set_purchase_price(self, purchase_price):
        '''
        This method sets the purchase price.
        
        Params:
        @purchase_price    Float - the current purchase price.
        '''
        self.purchase_price = purchase_price
    
    def set_quantity_available(self, quantity):
        '''
        This method sets the amount of units available for sale or rent.
        
        Params:
        @quantity    Integer - the amount of units available for sale or rent.
        '''
        self.quantity = quantity
    
    def get_code(self):
        '''
        Returns a String with the movie code. 
        '''
        return self.code
    
    def get_title(self):
        '''
        Returns a String with movie title. 
        '''
        return self.title
    
    def get_release_year(self):
        '''
        Returns an Integer with the movie's release year. 
        '''
        return self.release_year
    
    def get_stars(self):
        '''
        Returns an Array[String] with the main actors in the movie. 
        '''
        return self.stars
    
    def get_director(self):
        '''
        Returns a String with the movie's director. 
        '''
        return self.director
    
    def get_genres(self):
        '''
        return an Array[String] with all genres of the movie. 
        '''
        return self.genres
    
    def get_story_line(self):
        '''
        Returns a String with the story line. 
        '''
        return self.story_line
    
    def get_rating(self):
        '''
        Returns an Integer with the rating.
        '''
        return self.rating
    
    def get_ranking(self):
        '''
        Returns an Integer with the ranking.
        '''
        return self.ranking
    
    def get_rental_price(self):
        '''
        Returns a Float number with the rental price.
        '''
        return self.rental_price
    
    def get_purchase_price(self):
        '''
        Returns a Float number with the purchase price.
        '''
        return self.purchase_price
    
    def get_quantity_available(self):
        '''
        Returns an Integer with the amount of units available.
        '''
        return self.quantity

    def load_data(self, movie_data):
        '''
        This method initialize the movie data from a dictionary sent as parameter.
        
        Param:
        @movie_data    Dictionary that contains all movie's data.
        '''
        self.code = movie_data['code']
        self.title = movie_data['title']
        self.release_year = movie_data['release_year']
        self.stars = movie_data['stars']
        self.director = movie_data['director']
        self.genres = movie_data['genres']
        self.story_line = movie_data['story_line']
        self.rating = movie_data['rating']
        self.ranking = movie_data['ranking']
        self.rental_price = movie_data['rental_price']
        self.purchase_price = movie_data['purchase_price']
        self.quantity = movie_data['quantity']

    def save(self):
        '''
        This saves the movie information persistently into database.
        '''
        movie_query = "INSERT INTO %s VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" % self.table
        object_data = (self.code, self.title, self.release_year, self.director, self.story_line,
                self.rating, self.ranking, self.rental_price, self.purchase_price, self.quantity)
        try:
            db_connection = self.db_handler.connect()
            actor_ids = self.prepare_stars_to_save(db_connection)
            genre_ids = self.prepare_genres_to_save(db_connection)
            db_connection.execute(movie_query, object_data)
            for actor_id in actor_ids:
                db_connection.execute("INSERT INTO MOVIE_ACTOR VALUES(?, ?)", (self.code, actor_id))
            for genre_id in genre_ids:
                db_connection.execute("INSERT INTO MOVIE_GENRE VALUES(?, ?)", (self.code, genre_id))
            db_connection.commit()
        except Exception, error:
            db_connection.rollback()
            print "Error saving movie data: %s:" % error.args[0]
        finally:
            self.db_handler.close_connection()

    def prepare_stars_to_save(self, db_connection):
        '''
        This method prepare the actors to be saved into database. It is used for transactions.
        Returns an Array[Int] with all actor's ids.
        
        @db_connection    sqlite3.connect object used to prepare the db transaction.
        '''
        actor_ids = []
        for actor_name in self.stars:
            actor = Actor(actor_name)
            actor_ids.append(actor.prepare_to_create(db_connection))
        return actor_ids
    
    def prepare_genres_to_save(self, db_connection):
        '''
        This method prepare the genres to be saved into database. It is used for transactions.
        Returns an Array[Int] with all genre's ids.
        
        @db_connection    sqlite3.connect object used to prepare the db transaction.
        '''
        genre_ids = []
        for genre_name in self.genres:
            genre = Genre(genre_name)
            genre_ids.append(genre.prepare_to_create(db_connection))
        return genre_ids
