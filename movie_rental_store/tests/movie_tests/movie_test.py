
import unittest

import os
import collections
from database.database_connection import DataBase
from modules.entity.movie import Movie

class MovieTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        Create a database for testing purpose, and initialize the movie data.
        '''
        self.create_database()
        self.initialize_movie_data()
    
    @classmethod
    def create_database(self):
        self.database_name = 'DB_MOVIE_RENTAL.db'
        db_connection = DataBase(self.database_name)
        movie_table = (
            "CREATE TABLE MOVIE(code VARCHAR PRIMARY KEY NOT NULL, title VARCHAR NOT NULL, "
            "release_year INTEGER NOT NULL, director VARCHAR NOT NULL, story_line VARCHAR, "
            "rating INTEGER, ranking INTEGER, rental_price FLOAT, purchase_price FLOAT, quantity INTEGER)")
        actor_table = "CREATE TABLE ACTOR(actor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR NOT NULL)"
        genre_table = "CREATE TABLE GENRE(genre_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR NOT NULL)"
        movie_actor = "CREATE TABLE MOVIE_ACTOR(movie_code VARCHAR NOT NULL, actor_id INTEGER NOT NULL, PRIMARY KEY(movie_code, actor_id))"
        movie_genre = "CREATE TABLE MOVIE_GENRE(movie_code VARCHAR NOT NULL, genre_id INTEGER NOT NULL, PRIMARY KEY(movie_code, genre_id))"
        db_connection._execute_query(movie_table)
        db_connection._execute_query(actor_table)
        db_connection._execute_query(genre_table)
        db_connection._execute_query(movie_actor)
        db_connection._execute_query(movie_genre)
        db_connection.close_connection()
    
    @classmethod
    def initialize_movie_data(self):
        self.movie = Movie()
        self.data = collections.OrderedDict()
        self.data['code'] = 'mov01'
        self.data['title'] = 'Movie Name'
        self.data['release_year'] = 2015
        self.data['director'] = 'Unknown'
        self.data['story_line'] = 'Movie description'
        self.data['stars'] = []
        self.data['rating'] = 25
        self.data['ranking'] = 10
        self.data['genres'] = ['horror', 'misc']
        self.data['rental_price'] = 2.5
        self.data['purchase_price'] = 10.25
        self.data['quantity'] = 5
    
    @classmethod
    def tearDownClass(self):
        '''
        Insert a Table into database to perform and test the database operations.
        '''
        os.remove(self.database_name)

    def test_load_movie_data_from_dictionary(self):
        self.movie.load_data(self.data)
        current_object_data = [self.movie.get_code(), self.movie.get_title(), self.movie.get_release_year(),
                               self.movie.get_director(), self.movie.get_story_line(), self.movie.get_stars(),
                               self.movie.get_rating(), self.movie.get_ranking(), self.movie.get_genres(),
                               self.movie.get_rental_price(), self.movie.get_purchase_price(),
                               self.movie.get_quantity_available()]
        expected_data = self.data.values()
        self.assertEqual(current_object_data, expected_data)

    def test_saved_movie_is_stored_into_database(self):
        self.movie.save()
        db_connection = DataBase(self.database_name)
        movie_stored_data = db_connection.select("SELECT * FROM MOVIE")
        expected_movie_data = [('mov01', 'Movie Name', 2015, 'Unknown', 'Movie description', 25, 10, 2.5, 10.25, 5)]
        self.assertEqual(movie_stored_data, expected_movie_data)
        actor_stored_data = db_connection.select("SELECT * FROM ACTOR")
        expected_actor_data = []
        self.assertEqual(actor_stored_data, expected_actor_data)
        genre_stored_data = db_connection.select("SELECT * FROM GENRE")
        expected_genre_data = [(1, 'horror'), (2, 'misc')]
        self.assertEqual(genre_stored_data, expected_genre_data)
        movie_actor_stored_data = db_connection.select("SELECT * FROM MOVIE_ACTOR")
        expected_movie_actor_data = []
        self.assertEqual(movie_actor_stored_data, expected_movie_actor_data)
        movie_genre_stored_data = db_connection.select("SELECT * FROM MOVIE_GENRE")
        expected_movie_genre_data = [('mov01', 1), ('mov01', 2)]
        self.assertEqual(movie_genre_stored_data, expected_movie_genre_data)

if __name__ == "__main__":
    unittest.main()