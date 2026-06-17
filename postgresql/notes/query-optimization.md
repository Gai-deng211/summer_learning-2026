## Date: June 16, 2026
# PostgreSQL Performance Optimization – Indexing Experiment

## What I Built
- Generated and managed a large-scale synthetic dataset of **500,000 job records** using Python (Faker + SQLAlchemy).
- Designed SQL queries to simulate real-world job search workloads (filtering, sorting, limiting results).
- Used `EXPLAIN ANALYZE` to study PostgreSQL query execution behavior before and after indexing.

---

## Performance Optimization Experiment

### BEFORE Index (Full Table Scan)
- Query type: Sequential Scan + Sort
- Execution time: **57.923 ms**
- Rows scanned: **500,000+**
- Strategy:
  - Full parallel scan of table
  - In-memory sorting of filtered results
  - High CPU + memory usage

---

### AFTER Index (B-Tree on salary DESC)
- Query type: Index Scan
- Execution time: **0.202 ms**
- Rows scanned: Only matching index range
- Strategy:
  - Direct traversal using indexed salary field
  - No full sort required
  - Minimal data access

---

## 📊 Performance Improvement

| Metric | Before Index | After Index | Improvement |
|--------|-------------|-------------|-------------|
| Execution Time | 57.923 ms | 0.202 ms | **~99.65% faster** |
| Relative Speed | 1x | ~286x faster | **~286× improvement** |
| Rows Processed | ~500,000 | Only filtered subset | Massive reduction |

---

## Key Technical Takeaways
- Learned how PostgreSQL query planner chooses between **Seq Scan vs Index Scan**
- Understood how **B-Tree indexes eliminate full scans and sorting overhead**
- Observed real-world performance impact of indexing on large datasets
- Applied `EXPLAIN ANALYZE` to benchmark query execution scientifically

---

## Engineering Insight
This experiment demonstrated how database indexing can reduce query execution time from **human-perceivable delay (~58ms)** to **near-instant response (~0.2ms)**, a ~99.65% improvement, which is critical for scalable backend systems handling large datasets.