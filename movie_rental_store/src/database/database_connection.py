
import sqlite3

class DataBase(object):
    '''
    This class set a data_base connection. 
    '''


    def __init__(self, database_name):
        '''
        Constructor
        '''
        self._database_name = database_name
        self._connection = None
    
    def connect(self):
        '''
        This method creates the data_base connection
        '''
        self._connection = sqlite3.connect(self._database_name)
    
    def close_connection(self):
        '''
        This method closes the data_base connection  
        '''
        self._connection.close()
    
    def select(self, query):
        '''
        This method executes a query and return the result as Bi-dimensional Array.
        If not any row is retrieved, it returns an empty array.
        
        Params:
        @query    String with the SQL query to retrieve the data from database 
        '''
        try:
            self.connect()
            cursor = self._connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
        except sqlite3.Error, error:
            print "Database error: %s:" % error.args[0]
        finally:
            self.close_connection()
        return result_set
    
    def _execute_query(self, query):
        '''
        This method executes a query to change the database status.
        It returns an Integer with the number of rows affected by the query execution.
        If not any row is affected, it returns -1 by default.
        
        Params:
        @query    String that contains the SQL query 
        '''
        try:
            self.connect()
            cursor = self._connection.cursor()
            cursor.execute(query)
            self._connection.commit()
        except sqlite3.Error, error:
            self._connection.rollback()
            print "Database error: %s:" % error.args[0]
        finally:
            self.close_connection()
        return cursor.rowcount
    
    def insert(self, query):
        '''
        This method executes a query to insert new data.
        It returns an Integer with the number of rows inserted.
        If not any row is inserted, it returns -1 by default.
        
        Params:
        @query    String that contains the SQL query 
        '''
        return self._execute_query(query)
    
    def update(self, query):
        '''
        This method executes a query to update existing data.
        It returns an Integer with the number of rows affected.
        If not any row is affected, it returns -1 by default.
        
        Params:
        @query    The SQL query 
        '''
        return self._execute_query(query)
    
    def delete(self, query):
        '''
        This method executes a query to delete data.
        It returns an Integer with the number of rows deleted.
        If not any row is deleted, it returns -1 by default.
        
        Params:
        @query    String that contains the SQL query 
        '''
        return self._execute_query(query)
