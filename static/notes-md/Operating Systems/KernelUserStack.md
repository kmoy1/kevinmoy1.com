# Kernel and User Stacks

When "stack" is referenced in technical terms, it often refers not just to the **user stack** but to the **kernel stack** as well. 

Each process has its own **virtual memory space**, which is divided into **user space** and **kernel space**. Kernel space is always above user space (higher memory address). 

The OS kernel provides services that can be accessed by a user process through **syscalls**. This allows user space to interface with kernel space. When a user process is running and using the user stack for stuff, we say our program is running in **user mode**. When a syscall is made, however, our program switches to **kernel mode**, where the kernel stack is used as our stack for the duration of the syscall. *Kernel mode the only way to access the kernel stack*: it cannot be accessed by a program in user mode. 

While the size of a user stack is not fixed, the kernel stack is, typically two pages (8 KiB) reserved for each thread (remember each thread has its own kernel stack). 

The separation of the user and kernel stack is yet another example of isolation: a user stack crash cannot crash the kernel, and vice versa. 

