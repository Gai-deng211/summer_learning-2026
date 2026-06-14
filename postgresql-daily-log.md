# PostgreSQL + SQLAlchemy Daily Progress 
# DATE: June 13, 2026: BASIC PostgreSQL Engine Setup
### Summary
    - Today I successfully completed and validated my PostgreSQL + SQLAlchemy workflow in my Python project.
### What I accomplished
    -   Established a working connection to a PostgreSQL database using SQLAlchemy
    -   Confirmed successful DB connectivity with:
    -   Connection to the database successfully
    -   Executed SQL queries and retrieved structured results from the database
    -   Printed query results as Python dictionaries using _mapping, improving readability:
        {'id': ..., 'name': ..., 'email': ..., 'joined_at': ...}
### Key concepts reinforced
    -   SQLAlchemy engine setup and connection lifecycle
    -   Executing raw SQL using text() queries
    -   Fetching and iterating over query results
    -   Understanding PostgreSQL role-based access (RBAC basics)
    -   Working with timestamps (datetime) returned from PostgreSQL
    -   Using environment variables securely via .env and load_dotenv()
    🔧 Development workflow

### Used Git workflow:
    - staged changes with git add .
    - committed with a structured learning-focused message
    - pushed successfully to GitHub repository
### This session solidified my understanding of:

    - Python ↔ PostgreSQL integration
    - SQLAlchemy as a database abstraction layer
    - Clean data output formatting for backend development

## File Structure - See the files here for the source code. 
```
summer_learning_2026/
└── postgresql/
    └── app/
        ├── psql-engine-setup.py     # ⬅️ Connection strings, raw sql queries here
        └── .env                     # ⬅️ Database URL here as environment variable for security (No visible, remained in the local computer)
 ```      