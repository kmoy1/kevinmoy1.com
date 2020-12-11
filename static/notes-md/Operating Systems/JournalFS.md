# Journaling File System

A file system that uses **journaling** is one that keeps track of file changes in a special kind of log called a *journal* (also called a *transaction log*). Before an Xact (1+ file changes) is committed, it is logged *first*. If recovery is needed (e.g. on power failure or a machine crash), we can utilize our journal to restore to a consistent state.

Depending on implementation, journaling file systems can store either file metadata OR both data and file metadata. The former comes, of course, with improved performance, as there's less shit to store. The journal can also be fixed-size or dynamic, also depending on implementation. 

File updates often take multiple (write) operations. For example, deleting a UNIX file has three steps:

1. Deleting directory entry
2. Freeing file inode-> **inode pool**
3. Freeing file disk blocks (data blocks) -> **disk block pool**

What if our system crashes after step 1 but before step 2? We have an *orphaned inode* (one with no corresponding directory entry) and therefore it cannot be reached, resulting in a **memory leak**. 

Without a journal, the normal recovery process would be rather cumbersome: we would have to walk through the entire file's data structures (its directories, inode, disk blocks). This can take a while, especially if **I/O bandwidth** is small. 

But with a journal, we know our intended changes are already recorded at "crashpoint". Recovery, then, is simply reading and replaying changes (ATOMICALLY) until our file system is consistent again. So we either end up fully completing our Xact during recovery OR just not doing it at all, which is absolutely what we want- we certainly don't want to leave our file system in an intermediate state. 

