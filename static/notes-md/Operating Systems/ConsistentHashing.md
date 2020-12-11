# Consistent Hashing (TODO)

**Consistent hashing** is a special hashing design such that on hash table resize, the number of *key remappings* is minimized.

Specifically, given a hash table with $n$ keys and $m$ buckets (or "slots"), when we resize our consistently-hashed table, we only need to remap $\frac{n}{m}$ keys on average. Normally, all $n$ keys would have to be remapped! Another way to think about consistent hashing is that our *hash function changes minimally* as its range changes (more buckets!) 

This becomes particularly important in distributed computing. But before we understand consistent hashing, we must first learn about **distributed hashing**. 

## Distributed Hashing

Suppose we are trying to manage employee information at a **highly* trending startup company. We keep all employee info in a hash table (say, mapping employee ID to a string of their personal info). But here's the issue: because our company is getting really popular, employees keep rolling in and getting hired. Suddenly, it becomes difficult to fit the huge employee hash table onto a single computer. 

So we try to distribute our hash table to *multiple* computers (we'll call them *servers* from here on out, for generalization). To do this, we must redistribute hash keys and objects (info strings). But how do we *distribute* such keys + objects among the servers? 

