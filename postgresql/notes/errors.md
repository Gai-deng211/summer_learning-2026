# Errors and Fixes

## WEEK1: 
### DATE: June 12, 2056

#### Password Authentication Failed

    Error:
        FATAL: password authentication failed for user

    Cause:
        Incorrect PostgreSQL credentials.

    Fix:
        Use correct PostgreSQL role and password.

    Lesson:
        PostgreSQL users are independent of Linux users.