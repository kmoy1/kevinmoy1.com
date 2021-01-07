# Suffix Trees

Given a text string $S$, a **suffix tree** is a tree that contains each suffix of $S$ as a root-to-leaf path. Although the concept might seem weird, we'll see the presence of a suffix tree actually allows many string operations to be done in pretty fast runtime!

## Properties

The suffix tree of $S$ with length $|S| = n$ has two key tree properties:

- Because $S$ is length $n$, it has $n$ suffixes. Because there's exactly one root-to-leaf path per suffix, we know **our tree has $n$ leaf nodes.**
- Each internal node has at least two children: no "sticks".

## Runtime

Given a string $S$ with length $n$, a suffix tree for $S$ can be build in $\Theta(n)$ time. We will assume that the **alphabet** $\Sigma$ of $S$ is a constant-sized alphabet. 

## Applications

There are a surprisingly WIDE variety of algorithms a suffix tree can drastically improve. By far the most common use is being able to find a **query string** $P$ in $S$ in linear time to the query string. However, suffix trees can also solve other problems, such as both the **exact matching problem** *and* the **inexact matching problem**. 





