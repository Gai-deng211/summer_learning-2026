# Date: June 16, 2026
# Objective/Goal:
```
To Analyze Query Performance with EXPLAIN ANALYZE on 500k postgreSQL rows of data.
```
 ## Experiment 1:
```
No Index on salary column:
```

METRICS:
```
Planning Time: 0.470 ms
Execution Time: 43.650 ms
```


## Experiment 2:
```
Index created on salary column:
```

METRICS:
```
Planning Time: 0.248 ms
Execution Time: 0.163 ms
```


CONCLUSION
```
With no index on the salary column, query execution is slower. Adding an index can greatly improve query execution time.
```