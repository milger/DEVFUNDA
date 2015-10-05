
from database.database_connection import DataBase

class Actor(object):
    '''
    It defines an Actor object 
    '''


    def __init__(self, complete_name):
        '''
        Initialize a new Actor object 
        '''
        self.db_connection = DataBase('DB_MOVIE_RENTAL.db')
        self.table = "ACTOR"
        self.name = complete_name
    
    def create(self):
        '''
        This method saves the current object into database. If this actor already exist,
        it does not insert any data.
        '''
        existing_actor_id = self.get_actor_id()
        if existing_actor_id == None:
            actor_statement = "INSERT INTO %s(name) VALUES('%s')" % (self.table, self.name)
            self.db_connection.insert(actor_statement)
    
    def prepare_to_create(self, db_connection):
        '''
        This method prepare the current object to be saved into database using a sqlite3.connect object
        sent as parameter. It is used for transactions.
        Returns the actor_id as integer
        
        Params:
        @db_connection    sqlite3.connect object used to prepare the db transaction.
        '''
        existing_actor_id = self.get_actor_id()
        if existing_actor_id == None:
            actor_statement = "INSERT INTO %s(name) VALUES(?)" % self.table
            db_connection.execute(actor_statement, (self.name,))
            db_cursor = db_connection.cursor()
            query_id = "SELECT actor_id FROM %s WHERE name = '%s'" % (self.table, self.name)
            db_cursor.execute(query_id)
            result_set_actor_id = db_cursor.fetchone()
            existing_actor_id = result_set_actor_id[0]
        return existing_actor_id
    
    def get_actor_id(self):
        '''
        This method gets the id of this current actor object from database according its name.
        Returns an integer with the actor_id. IF the actor is not found into database,
        it returns None
        '''
        actor_id = None
        query = "SELECT actor_id FROM %s WHERE name = '%s'" % (self.table, self.name)
        rows = self.db_connection.select(query)
        if len(rows) == 1:
            actor_id = rows[0][0]
        return actor_id

    def remove(self):
        '''
        This method deletes the current object from database.
        '''
        actor_sentence = "DELETE FROM %s WHERE name = '%s'" % (self.table, self.name)
        self.db_connection.delete(actor_sentence)
