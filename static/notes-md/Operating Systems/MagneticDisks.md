# Magnetic Disks

A **magnetic disk** is a storage device using magnetism, on a big platter. 

To read/write data from a magnetic disk, there is a three step process. First, the disk must position the head over the proper **track**: the concentric circle of the platter that contains the data we want. Then, the head must rotate to read the desired **sector** of our track, which is the actual reading of our data from disk. Finally, we wait for this sector to transfer under the head.

In total, the time that this read/write process takes is modeled as **seek time + rotational latency + transfer time**. When accounting for the entirety of the system, we must also account for the I/O request queue and disk controller as well. Therefore we add two terms: **queueing time ** and **controller time** as part of the total read/write time.