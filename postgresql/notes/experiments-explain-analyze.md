# Date: June 16, 2026
# Objective/Goal:
```
To Analyze Query Performance with EXPLAIN ANALYZE on 500k postgreSQL rows of data.
```
 ## Experiment 1:
Constrain:
```
No Index on salary column:
```

Metrics:
```
Planning Time: 0.628 ms
Execution Time: 84.754 ms
```


## Experiment 2:
Constraint:
```
Index created on salary column:
```

Metrics:
```
Planning Time: 0.508 ms
Execution Time: 0.266 ms
```


Conclusion
```
With no index on the salary column, query execution is slower. Adding an index can greatly improve query execution time.
```