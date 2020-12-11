# Memory Segments

Von Neumann architecture hinges on the fact that *programs can be treated as data*, and thus storing instructions and data in the same memory. Thus, we divide memory into four different segments: a **stack segment**, a **heap segment**, a **data segment**, and a **code segment**.

Let's explore what the purpose of each of these segments are. 

## Stack Segment

The **stack segment** contains the ever-important **user stack**, which is used as temporary storage during program execution. It is basically a fixed-size block of memory, and grows *downward* (from high memory address to low) as elements are **pushed** onto the stack. The **stack pointer** (`%esp` register in x86) always points to the top of the stack, and moves accordingly as elements are pushed/popped off the top.

## Heap Segment

The **heap segment** is a chunk of memory used for **dynamic allocation** of memory- specifically those with the `(*)alloc` calls in C. The heap segment is actually just a specific example of a **memory pool**: a list of (fixed-size) memory blocks *ready for use on demand*. We will also see different kind of pools through operating systems, such as *thread pools* and *connection pools*.

Thus, like the stack segment, heap size is variable. However, unlike the stack segment, it grows *upward*. 

## Data Segment

The **data segment** (sometimes called the static segment) contains **static program data**: variables that don't change (static) through program execution. These include global variables and other data specifically declared static. There's also another exception in C with **string literals** (also called "string constants"), which are manually-typed out strings enclosed with double quotes:

```C
char* stringLiteral = "Oh Blocked by James!"; //stored in data/static segment
char x[15];
```

## Code Segment

Finally, the **code segment** (also called text segment) contains our program instructions- basically, the lines of code to be executed. Specifically it contains the program's **machine instructions** or **assembly code**. 

 