# Parsimony

**Parsimony** (also known in some contexts as *Occam's razor*) is the principle that the simplest explanation for an event is best. In the case of evolutionary history, we would prefer explanations of taxa through the smallest number of mutations (changes). 

A **character** (denoted $\chi_i$) is an attribute that each (modern) member possesses. The evolutionary tree provides a **branching order** of evolutionary history to lead to these members, all diverging from some common ancestor from a long time ago. 

For these notes, only **binary-character** problems will be considered, where $\chi_i$ is either 0 or 1: either the member possesses the attribute or it does not. The major focus will be on the (binary) **perfect phylogeny** problem, which is a special case of the **maximum-parsimony** problem.

We can define our **character matrix** $M$ as an $n \times m$ matrix, with $n$ **taxa** and $m$ characters. $M[i,j]$ represents the $j$-th character of object $i$, and can either be 0 or 1 depending on whether that object possesses the character or not. 

From this matrix, we want to reconstruct a **phylogenetic tree** $T$ that explains the evolutionary history of its $n$ leaves (one leaf node per taxa). Additionally, each of the $m$ characters labels exactly ONE edge of $T$, so there will be exactly $m$ labeled edges in $T$. Finally, for each object (taxa) $p$, the root-to-leaf path for that object will specify ALL the characters of $p$ that have state 1. That means that our tree $T$ is **zero-rooted**. 

There are a couple more properties, such as a character can only mutate **exactly once.** This means that all child nodes below a particular edge with a character label will definitely possess that attribute! 

So what's so cool about finding such a tree given our input 

## Perfect Phylogeny

This leads us to the perfect phylogeny problem: given an $n \times m$ matrix $M$, can we reconstruct a phylogenetic tree $T$ that obeys all the above conditions? Sometimes we can find such a tree, and sometimes it's just impossible. When can we? 

There exists a pretty simple $O(mn)$-time algorithm to find such a tree (or report none exists). Let's run through it. 

The first thing we must do is **reorder the columns of** $M$. We do this by simply treating each column as a binary number and sorting in descending order. Let $\bar{M}$ represent the column-sorted $M$. This won't affect anything: obviously, if we know that $M$ has a phylogenetic tree iff $\bar{M}$ does. We will represent a given character $\chi_i$ as the $i$-th column (and its binary number) in $\bar{M}$. 

Now, for any column $k$ (character $\chi_k$) in $\bar{M}$, let $O_k$ be the taxa (rows) that contain 1 for that character. Then if $O_j \subset O_k$ then we know that $\chi_k$ must be to the left of $\chi_j$ in $\bar{M}$. Additionally, we know any duplicate characters will be contiguous. Thus we can state the basic theorem that grounds the perfect phylogeny algorithm:

**Matrix $M$ has a phylogenetic tree iff for every pair of characters $\chi_i, \chi_j$ in $\bar{M}$,  either $O_i$ and $O_j$ are disjoint OR one contains the other**. That means if any characters in M have "overlapping columns" like this

01
11
10

then we know that no phylogenetic tree exists. Let's prove this.

## Perfect Phylogeny Theorem: Forward Proof

First, we will prove that if $T$ exists, then for any pair of characters $\chi_i$ and $\chi_j$, either $O_i$ and $O_j$ are disjoint OR one contains the other. 

Let $T$ be our phylogenetic tree for $M$. Consider two characters $\chi_i$ and $\chi_j$. Since $T$ exists, we know $\chi_i$ and $\chi_j$ mutate exactly once, and have a representative tree edge for this. Let $e_i$ and $e_j$ be these edges. Then, all leaves (objects) that posses $\chi_i$ or $\chi_j$ are below $e_i$ and $e_j$ respectively. Then, one of four possible cases must hold, and all prove either one of two things: either $O_i$ and $O_j$ are disjoint OR one contains the other.

1.  $e_i = e_j$. Then, $O_i = O_j$. Done. 
2. $e_i$ is in the path from $T$'s root to $e_j$ ("**upstream**" from $e_j$). Then, all leaves below $e_j$ are also leaves below $e_i$, which means that $O_j \subseteq O_i$. Done.
3. $e_i$ is in the path from $e_j$ to one of $e_j$'s leaves ("**downstream**" from $e_j$). You could also just flip $e_i$ and $e_j$ in case 2. Then, all leaves below $e_i$ are also leaves below $e_j$, which means that $O_i \subseteq O_j$. Done.
4. $e_i$ and $e_j$ are not connected by any common path (they **diverge**). Then, the leaf sets are disjoint, and $O_i, O_j$ are therefore disjoint as well. Done.

## Perfect Phylogeny Theorem: Backward Proof

Now we will prove that if for any pair of characters $\chi_i$ and $\chi_j$ in $M$, that if the condition holds that either $O_i$ and $O_j$ are disjoint OR one contains the other, then a phylogenetic tree $T$ must exist. 

Consider two objects (rows) $p$ and $q$ in $\bar{M}$. Let $\chi_k$ be the **right-most** character that both $p$ and $q$ possess. Then, if $p$ possesses a character $\chi_i < \chi_k$ then we know $q$ must also possess $\chi_k$ as well. Why? We know that $O_i$ and $O_k$ intersect (since $p$ contains both characters)- specifically, we know $O_k \subseteq O_i$ and thus $q$ must possess $\chi_i$. 

We can formalize this by saying $\bar{M}[p, i] = \bar{M}[q, i]$ for every character $\chi_i < \chi_k$. Additionally, $\bar{M}[p, j] = \bar{M}[q, j]$ for $\chi_j > \chi_k$ iff $\bar{M}[p,j] = M[q,j] = 0$.

The rest of the proof involves **keyword trees** that will not be talked about here. 

## An $O(mn)$-time Perfect Phylogeny Algorithm

1. Sort columns of $M$ in decreasing order with radix sort to produce $\bar{M}$. Name each character $\chi_i$ by its column position $i$. 
2. For each row (object) $p$ in $\bar{M}$, find what characters $p$ possesses, and create a string out of them, until we have $n$ strings. 
3. Build a **keyword tree** $T$ given our $n$ strings. 
4. Test if $T$ is a perfect phylogenetic tree. If it isn't then no such tree exists. 

## Generalized Perfect Phylogeny

In **generalized perfect phylogeny**, characters can have more than 2 states. 

In that case, a perfect phylogeny for M is a directed tree T where each object labels exactly one leaf of T as before, but now edges are labeled with an ordered triple (c, x, y): character c transitioning from state x to state y. 

Here's the constraint in this case: **for a given character c, there may exist only one mutation to a state y**. In other words, each edge must contain a unique character c and ending state y. 

Now the **generalized perfect phylogeny problem** asks if given an $n \times m$ matrix $M$ where each character can take up to $r$ states has a phylogenetic tree or not. This problem is a well-known unsolved problem and *well* beyond the scope of these notes (and my head). 