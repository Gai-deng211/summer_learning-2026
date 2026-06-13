from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load all the environment variables
load_dotenv()

# Fetch the databse URL
db_url = os.getenv("DATABASE_URL")

# Check if a valid database url was fetched
if not db_url:
    raise ValueError("No environment variable corresponding to the provided database Url found!")

# Create a function to return the database engine
def get_db_connection():
    # A check to catch handles such as invalid login credentials (Incorrect connection strings)
    try:
        my_engine = create_engine(db_url)
        print('Connection to the database successfully')
        return my_engine
    
    except Exception as ex:
        print('Connection to the database failed due to the following error:\n', ex)
        return None

my_engine = get_db_connection()

if my_engine:
    with my_engine.begin() as connection:
        resutls = connection.execute(text("SELECT * FROM users WHERE name like '%Gai%' ORDER BY id asC LIMIT 3;"))
        
        for name in resutls:
            print(dict(name._mapping))
else:
    print(None)
    
    # print(resutls.fetchall())
    