# RAID

**RAID** stands for **Redundant Array of Independent Disks**, and is the combination of multiple disks into one or more logical units in an *array*. This is done to increase reliability (through redundancy) as well as performance of storage. 

A RAID system consists of multiple disks (or SSDs) working in parallel. There are multiple RAID levels, each optimized for a specific situation.

We'll assume that in a RAID system we have $n > 1$ disks to store our data.

## RAID 0: Striping

In a **RAID 0** system, we split our data into *blocks* that get split across all array drives. This process of dividing our data volume into blocks and splitting it across disks is called **striping**.	

RAID 0 is ideal for any NON-critical storage of data, where speedy reads/writes are prioritized over reliability. 

## RAID 1: Mirroring

In a **RAID 1** system, data is stored *twice*: once in data drive, and once more in a **mirror drive**. We also use this for good read/write speed. 

## RAID 5: Striping with Parity

This is the most common RAID level, with $n>3$ drives. Data is striped across all drives, and on one drive, we keep a 