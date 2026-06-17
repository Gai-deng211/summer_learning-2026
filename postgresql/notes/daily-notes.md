# WEEK1: 

## DATE: June 12, 2056
### What I Did
    - Installed PostgreSQL
    - Connected PostgreSQL using SQLAlchemy
    - Created a clean database environment
    - Learned PostgreSQL roles and permissions

### What Broke
    - Incorrect SQLAlchemy connection string
    - Password authentication errors
    - Database did not exist

### What I Learned
    - PostgreSQL users are roles
    - Databases exist inside the PostgreSQL server
    - SQLAlchemy only connects to existing databases

### Next Step
    - Build users table
    - Build posts table
    - Learn foreign keys
----

## Date: June 16, 2026
# Today’s Learning Summary (PostgreSQL + Backend Practice)

- Set up a PostgreSQL database and user roles, including managing permissions and authentication.
- Designed and created a structured `jobs` table with constraints:
  - `NOT NULL` fields
  - `CHECK` constraints for data validity (e.g., salary > 0)
  - Default timestamps using `CURRENT_TIMESTAMP`
- Generated and inserted large-scale synthetic data (10,000+ rows) using Python’s Faker module and SQLAlchemy.
- Practiced bulk inserts and learned the importance of batch processing for performance.
- Executed complex SQL queries:
  - Sorting data (ORDER BY salary DESC)
  - Filtering and limiting results
  - Aggregations using COUNT(*)
- Used `EXPLAIN ANALYZE` to inspect query execution plans and understand:
  - Sequential scans vs index scans
  - Query planning and execution time
- Learned foundational database performance concepts:
  - How indexes affect query speed
  - Trade-offs between full table scans and optimized access paths

# Key Takeaway
Built a complete mini backend data pipeline: from database setup → data generation → bulk insertion → querying → performance analysis.

