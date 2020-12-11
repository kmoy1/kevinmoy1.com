# Suffix Tree: Substring Algorithm

Let's examine how a suffix tree solves the **exact matching problem** (EMP).

First, let's understand what we're trying to do. Say we have a *reference text* $T$, with length $|T| = n$. Now let's say we have a *pattern*, or *query string*, $P$, with length $|P| = m$. The goal is to find **all** occurrences of $P$ in $T$ in linear $O(n+m)$ time (or report none exist). That means we only need to process the reference text and query string *once* for each query! Kind of neat!

The usage of suffix trees to solve this come with this algorithm:

```python
def EMP(P, T):
    """Find all occurrences of P in T in linear time"""
    ST = SuffixTree(T) #Generate suffix tree for reference text- O(n)
    subtree = traverse(P,ST) #Trace P along path in ST, until exhausted, and get the subtree
    return leaves(subtree) #IDs of leaves of subtree are occurrence indices of P in T!
```

Let's analyze this algorithm in full. We take in $P$ and $T$ and desire to return all occurrences of $P$- specifically, the indices where it occurs in $T$. The first thing we do is generate a suffix tree on $T$ via `SuffixTree(T)`: this takes $O(n)$ time. Then, tracing the pattern path along the suffix tree via `traverse(P,ST)` takes $O(m)$ time- the "work" at each node is constant. Finally, retrieving the leaves of this subtree, or the occurrences, takes $O(k)$ time with DFS, where $k$ is the number of actual occurrences of $P$ in $T$, but we can generally treat this as constant.

What is the purpose of this "tracing" of P along the suffix tree's path? We are utilizing the fact that **every substring of $T$ is a prefix of a suffix of $T$**.  This is exactly what we are checking for by tracing along a *path* in our suffix tree! Formally, $P$ occurs in $T$ at index $j$ if and only if $P$ is a prefix of suffix $j$ of $T$.  

Another important point is that $P$ **traces a unique path in the suffix tree**, as one of the ground rules of suffix trees is that *no two neighboring edges can begin with the same character*. 

## Only One Occurrence Needed

If only a *single* occurrence (say, the first) of $P$ in $T$ is required, then we can actually reduce search time from $O(m+k)$ to $O(m)$- meaning no DFS is needed. To do this, we need to mark each *internal* node of our suffix tree with the (smallest) suffix ID of its leaves. That way, we can just return this number and not do any leaf collecting.

We can mark our suffix tree in this way in the preprocessing stage, via (again) DFS, which takes $O(n)$ time- but done only once.

