import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Table, Column, Integer, String, Float, MetaData, inspect
from sqlalchemy.exc import OperationalError, ProgrammingError
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Database connection
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Encode the password to handle special characters
encoded_password = quote_plus(DB_PASSWORD)

# Construct the DATABASE_URL
DATABASE_URL = f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}/{DB_NAME}"

# Create the engine
engine = create_engine(DATABASE_URL)

# Define the database schema
metadata = MetaData()

progress = Table('progress', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('course', String),
    Column('lesson', String),
    Column('score', Float),
    Column('completed', Integer)
)

def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful.")
        return True
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
        return False

def check_database_exists():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print(f"Database '{DB_NAME}' exists.")
        return True
    except ProgrammingError:
        print(f"Database '{DB_NAME}' does not exist.")
        return False

def check_table_exists(table_name):
    inspector = inspect(engine)
    if table_name in inspector.get_table_names():
        print(f"Table '{table_name}' exists.")
        return True
    else:
        print(f"Table '{table_name}' does not exist.")
        return False

def check_create_table_permission():
    try:
        with engine.connect() as connection:
            connection.execute(text("CREATE TABLE test_permissions (id INTEGER PRIMARY KEY)"))
            connection.execute(text("DROP TABLE test_permissions"))
        print("User has permission to create tables.")
        return True
    except Exception as e:
        print("User does not have permission to create tables.")
        print("To grant the necessary permissions, a database administrator should run the following commands:")
        print(f"GRANT CREATE ON SCHEMA public TO {DB_USER};")
        print(f"GRANT USAGE ON SCHEMA public TO {DB_USER};")
        return False

def create_tables():
    if not check_table_exists('progress'):
        if check_create_table_permission():
            try:
                metadata.create_all(engine)
                print("Table 'progress' created successfully.")
            except Exception as e:
                print(f"Error creating table: {e}")
        else:
            print("Unable to create table due to insufficient permissions.")
    else:
        print("Table 'progress' already exists.")

def seed_initial_data():
    # Add any initial data seeding here if needed
    pass

def setup_database():
    if test_connection() and check_database_exists():
        create_tables()
        seed_initial_data()
        print("Database setup completed.")
    else:
        print("Database setup failed.")

if __name__ == "__main__":
    setup_database()