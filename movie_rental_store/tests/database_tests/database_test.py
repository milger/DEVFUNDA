
import unittest
import os
from database.database_connection import DataBase


class DatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        Create a database for testing purposes.
        '''
        self.database_name = 'testBD.db'
        self.db_connection = DataBase(self.database_name)
        self.db_connection._execute_query("CREATE TABLE User (name, role)")

    @classmethod
    def tearDownClass(self):
        '''
        Insert a Table into database to perform and test the database operations.
        '''
        os.remove(self.database_name)

    def test1_database_is_created_after_connection(self):
        self.assertTrue(os.path.exists(self.database_name))

    def test2_execute_an_insert_query(self):
        insert_query = "INSERT INTO User SELECT 'Jhon', 1 UNION SELECT 'Paul', 1 UNION SELECT 'Anna', 2"
        affected_rows = self.db_connection.insert(insert_query)
        self.assertEqual(affected_rows, 3)

    def test3_execute_a_select_query(self):
        select_query = "SELECT * FROM User WHERE role = 1"
        expected_result = [('Jhon', 1), ('Paul', 1)]
        result_set = self.db_connection.select(select_query)
        self.assertEqual(result_set, expected_result)

    def test4_execute_an_update_query(self):
        update_query = "UPDATE User SET role = 3 WHERE role = 1"
        affected_rows = self.db_connection.update(update_query)
        self.assertEqual(affected_rows, 2)

    def test5_execute_a_delete_query(self):
        delete_query = "DELETE FROM User"
        affected_rows = self.db_connection.delete(delete_query)
        self.assertEqual(affected_rows, 3)

if __name__ == "__main__":
    unittest.main()
