# Date: June 16, 2026
# Objective/Goal:
```
To Analyze Query Performance with EXPLAIN ANALYZE on 500k postgreSQL rows of data.
```
 ## Experiment 1:
Constraint:
```
No Index on salary column:
```

Metrics:
```
Planning Time: 0.878 ms
Execution Time: 74.361 ms
```


## Experiment 2:
Constraint:
```
Index created on salary column:
```

Metrics:
```
Planning Time: 0.643 ms
Execution Time: 0.401 ms
```


Conclusion
```
With no index on the salary column, query execution is slower. Adding an index can greatly improve query execution time.
```