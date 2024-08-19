import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Table, Column, Integer, String, Float, MetaData
from sqlalchemy.orm import sessionmaker
import pandas as pd
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
Session = sessionmaker(bind=engine)

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

# Remove the following line as it's now handled in db_setup.py
# metadata.create_all(engine)

def update_progress(user_id, course, lesson, score, completed):
    with Session() as session:
        existing = session.query(progress).filter_by(
            user_id=user_id, course=course, lesson=lesson
        ).first()
        
        if existing:
            existing.score = score
            existing.completed = completed
        else:
            new_progress = progress.insert().values(
                user_id=user_id, course=course, lesson=lesson, 
                score=score, completed=completed
            )
            session.execute(new_progress)
        
        session.commit()

def get_progress(user_id):
    with engine.connect() as conn:
        query = text(f"SELECT * FROM progress WHERE user_id = :user_id ORDER BY course, lesson")
        result = conn.execute(query, {"user_id": user_id})
        return pd.DataFrame(result.fetchall(), columns=result.keys())

def reset_progress(user_id, courses=None, lessons=None):
    with Session() as session:
        query = session.query(progress).filter_by(user_id=user_id)
        
        if courses:
            query = query.filter(progress.c.course.in_(courses))
        if lessons:
            query = query.filter(progress.c.lesson.in_(lessons))
        
        query.delete(synchronize_session='fetch')
        session.commit()

def get_courses_and_lessons(user_id):
    with engine.connect() as conn:
        query = text("""
        SELECT DISTINCT course, lesson 
        FROM progress 
        WHERE user_id = :user_id
        ORDER BY course, lesson
        """)
        result = conn.execute(query, {"user_id": user_id})
        
        courses_lessons = {}
        for row in result:
            course, lesson = row
            if course not in courses_lessons:
                courses_lessons[course] = []
            courses_lessons[course].append(lesson)
        
        return courses_lessons

def test_env_values():
    print("Testing .env values:")
    print(f"DB_USER: {'*' * len(DB_USER) if DB_USER else 'Not set'}")
    print(f"DB_PASSWORD: {'*' * len(DB_PASSWORD) if DB_PASSWORD else 'Not set'}")
    print(f"DB_HOST: {DB_HOST if DB_HOST else 'Not set'}")
    print(f"DB_NAME: {DB_NAME if DB_NAME else 'Not set'}")
    print(f"\nConstructed DATABASE_URL: {DATABASE_URL.replace(encoded_password, '*' * len(encoded_password))}")

    if all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
        print("\nAll required environment variables are set.")
    else:
        print("\nWARNING: Some required environment variables are missing!")

def test_database_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Database connection successful!")
            print("Query result:", result.fetchone())
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return False

if __name__ == "__main__":
    test_env_values()
    print("\n" + "="*50 + "\n")
    test_database_connection()