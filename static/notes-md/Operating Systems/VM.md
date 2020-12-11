# Virtual Memory

In modern memory systems, memory is almost *never* accessed directly, as this can lead to a lot of hacking and privacy issues. So...how do we access memory?

Pretty much all modern operating systems implement something called **virtual memory**, where a *virtual address space* (called "user space") maps a user-perspective memory address to the actual physical memory address through a process called *translation*. 

To implement the virtual memory system, virtual AND physical memory are divided up into fixed-size chunks called **pages**, most commonly with 4 KiB (4096 bytes) size. 

There are many uses for virtual memory. One of the most important is that of **memory isolation**: a process's memory space is protected from other processes. When processes want to share memory (perhaps for communication), there's less memory management overhead involved. Additionally, through an on-demand page provision service fittingly called **demand paging**, we can give processes the illusion that THEIR memory is pretty much infinite. Even better, our system can actually perform **swapping** as well, where inactive pages are simply swapped to the hard drive for performance optimization. 