# BWT 2: How it Works

This note will run through how BWT is implemented in practice. We know from the intro note that BWT was naively done by sorting a block of string rotations, then grabbing the last column, which seems like a lot of work. But there's plenty of ways to make this faster- specifically, to $O(n)$ runtime: let's get to it. 

Before we grind, though, let's establish a few ground variables. We will refer to our transformed string as $S$, with length $|S| = n$. The alphabet is $\Sigma$ where the sentinel '\$' is always "less than" all characters in our alphabet. 

## Forward BWT

The **forward BWT** is the process we're familiar with from the intro note: sorting all rotations of $T$ into a matrix.