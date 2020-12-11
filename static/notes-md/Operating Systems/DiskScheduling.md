# Disk Scheduling

Remember that a process's runtime, or **burst time**, is divided between CPU time and IO time. In particular, I/O time makes a request to the operating system to access (read/write) the disk.  In the same exact way the CPU has a scheduler to allocate CPU to processes, the disk has a scheduler to determine which I/O request gets DISK time. 

Ideally, a good disk scheduling algorithm will be:

1. Fair to all requests (no starvation)
2. High throughput (requests completion rate)
3. Minimal head movement time: we certainly don't want to make an entire rotation for every single access. 

There are several good disk scheduling algorithms. The most natural is FCFS: First Come First Served, but this has limitations in fairness. Other algorithms are **Shortest Seek Time First** (SSTF) as well as SCAN and C-SCAN scheduling. We'll discuss some of these algorithms below.

## Shortest Seek Time First (SSTF)

## SCAN (Elevator Algorithm)

  

## C-SCAN
