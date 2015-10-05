
from database.database_connection import DataBase

class Genre(object):
    '''
    It defines Genre object 
    '''


    def __init__(self, name):
        '''
        Initialize a new Genre object 
        '''
        self.db_connection = DataBase('DB_MOVIE_RENTAL.db')
        self.table = "GENRE"
        self.name = name
    
    def create(self):
        '''
        This method saves the current object into database. If this genre already exist,
        it does not insert any data.
        '''
        existing_genre_id = self.get_genre_id()
        if existing_genre_id == None:
            genre_statement = "INSERT INTO %s(name) VALUES('%s')" % (self.table, self.name)
            self.db_connection.insert(genre_statement)
    
    def prepare_to_create(self, db_connection):
        '''
        This method prepare the current object to be saved into database using the sqlite3.connect object.
        It is used for transactions. Returns the genre_id as integer
        
        Params:
        @db_connection    sqlite3.connect object used to prepare the db transaction. 
        '''
        existing_genre_id = self.get_genre_id()
        if existing_genre_id == None:
            genre_statement = "INSERT INTO %s(name) VALUES(?)" % self.table
            db_connection.execute(genre_statement, (self.name,))
            db_cursor = db_connection.cursor()
            query_id = "SELECT genre_id FROM %s WHERE name = '%s'" % (self.table, self.name)
            db_cursor.execute(query_id)
            result_set_genre_id = db_cursor.fetchone()
            existing_genre_id = result_set_genre_id[0]
        return existing_genre_id
    
    def get_genre_id(self):
        '''
        This method gets the id of this current object from database according its name.
        Returns an integer with the genre_id. IF the genre is not found into database,
        it returns None
        '''
        genre_id = None
        query = "SELECT genre_id FROM %s WHERE name = '%s'" % (self.table, self.name)
        rows = self.db_connection.select(query)
        if len(rows) == 1:
            genre_id = rows[0][0] 
        return genre_id

    def remove(self):
        '''
        This method deletes the current object from database.
        '''
        genre_statement = "DELETE FROM %s WHERE name = '%s'" % (self.table, self.name)
        self.db_connection.delete(genre_statement)
