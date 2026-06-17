from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from faker import Faker
import os

# Load the environment variables
load_dotenv()

# Database URL
db_url = os.getenv("FAKER_URL")

# Check if the URL is valid
if not db_url:
    raise ValueError("No valid url found, please double-check the environment file!")

# Reusable database connection function with improved error handling and clear structure
def get_db_engine():
    """
    Returns a SQLAlchemy engine connected to the database specified in FAKER_URL.
    If connection fails, returns None and prints the error.
    Returns:
        engine (sqlalchemy.Engine or None): SQLAlchemy Engine instance if successful, None otherwise.
    """
    try:
        engine = create_engine(db_url)
        return engine
    except:
        return None

def create_job_table():
    """
    Creates the 'jobs' table in the database if it does not exist already.
    Uses the engine from get_db_engine(). Handles failures gracefully.
    """
    engine = get_db_engine()
    if not engine:
        print('❌❌❌ Database connection failed. Could not create table.')
        return

    try:
        with engine.connect() as conn:
            print('✅✅✅ Connected to the database successfully!')
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    company VARCHAR(255) NOT NULL,
                    location VARCHAR(255) NOT NULL,
                    salary INTEGER NOT NULL CHECK (salary > 0),
                    description TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            """))
            conn.commit()
            print('✅✅🚀 "jobs" table was created in the database successfully!')
    except Exception as ex:
        print(f'❌❌❌ Failed to create table: {str(ex).splitlines()[0]}')

fake = Faker()

def generate_jobs():
    """
    Generates a dictionary containing fake job data. The data includes a job title, company name, location, salary,
    and a brief description.

    Returns:
        dict: A dictionary with the following key-value pairs:
            - "title": str, randomly generated job title
            - "company": str, randomly generated company name
            - "location": str, randomly generated city
            - "salary": int, randomly generated salary between 40,000 and 200,000
            - "description": str, randomly generated text with up to 200 characters
    """
    return {
        "title": fake.job(),
        "company": fake.company(),
        "location": fake.city(),
        "salary": fake.random_int(min=40000, max=200000),
        "description": fake.text(max_nb_chars=200)
    }
    
def create_batch(size):
    return [generate_jobs() for _ in range(size)]

def insert_jobs(size):
    engine = get_db_engine()
    
    
    batch = create_batch(size)
    try:
        with engine.connect() as conn:
            conn.execute(text(
                """
                INSERT INTO jobs (
                    title, company, 
                    location, 
                    salary, 
                    description
                    ) 
                VALUES(:title, 
                    :company, 
                    :location, 
                    :salary, 
                    :description
                    )
                """), batch 
                )
            conn.commit()
            print(f"{size} rows persisted!!✅🚀")
    except Exception as ex:
        print(F"❌❌❌ Failed to insert {size} jobs due to: \n", str(ex).splitlines()[0])

def create_index_on_salary():
    try:
        my_engine = get_db_engine()
        with my_engine.begin() as conn:
            conn.execute(
                text("""CREATE INDEX IF NOT EXISTS idx_jobs_salary ON jobs(salary DESC);""")
            )
            print("Index created! 🚀🚀✅✅")
            return
    except Exception as ex:
        print(f"❌❌🥲Failed to create index due to the error: \n{str(ex).splitlines()[0]}")
        return
if __name__ == '__main__':
    insert_jobs(10000)
    create_index_on_salary()
    