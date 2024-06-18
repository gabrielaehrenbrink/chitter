import os
from flask import g
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class DatabaseConnection:
    DEV_DATABASE_NAME = os.getenv('DEV_DATABASE_NAME', 'chitter')
    TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'chitter_test')

    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg.connect(
                f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost/{self._database_name()}",
                row_factory=dict_row
            )
            print("Database connection established.")
        except psycopg.OperationalError as e:
            raise Exception(f"Couldn't connect to the database {self._database_name()}! " \
                            f"Did you create it using `createdb {self._database_name()}`?") from e

    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    def execute(self, query, params=[]):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = (
        'DatabaseConnection.exec_params: Cannot run a SQL query as '
        'the connection to the database was never opened. Did you '
        'make sure to call first the method DatabaseConnection.connect` '
        'in your app.py file (or in your tests)?'
    )

    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)

    def _database_name(self):
        if self.test_mode:
            return self.TEST_DATABASE_NAME
        else:
            return self.DEV_DATABASE_NAME

def get_flask_database_connection(app):
    if not hasattr(g, 'flask_database_connection'):
        g.flask_database_connection = DatabaseConnection(
            test_mode=os.getenv('APP_ENV') == 'test'
        )
        g.flask_database_connection.connect()
    return g.flask_database_connection
