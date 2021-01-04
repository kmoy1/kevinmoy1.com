# R-perfect Phylogeny

Before, we assumed the root of our phylogenetic tree was a zero vector. Let's release this assumption to form **r-perfect phylogeny**: finding a phylogenetic tree for $M$ where the *state* of the root is arbitrary binary vector $r$. 

Formally, for a set of $m$ nontrivial characters $\chi_1,...\chi_m$, we have an r-perfect phylogeny if there exists a phylogenetic tree $T$ with character extensions $\chi_1',...,\chi_m'$ such that $\sum_{1\le i \le d}Ch(X_i',T) = d$ (remember that character extensions are a function on tree nodes that tell whether that node possesses that character or not). 

Let's explore some of this. 

## Root Unknown Case

**Theorem**: if a matrix $M$ has an $r$-perfect phylogeny for some vector $r$, then every row $r'$ in $M$ is also a valid $r'$-perfect phylogeny. In other words, the **root state will be exactly the same as one of the leaves**. 

Let's prove this. 

Let's assume $M$ has an $r$-perfect phylogeny for some vector $r$. Let $v$ be the leaf node that corresponds to $r'$. We can reconstruct a *new* perfect phylogeny for $M$, with $r'$ as the root, with the following steps:

1. Remove the original root of the tree. Since this is a binary tree, the removed root will leave two child nodes: we connect these two with an edge. 
2. Insert a node between $v$ and its parent, and **make this the new tree node**. 
3. Label the node with the same state as $v$ (its edge is thus unlabeled, of course).

We can formalize this algorithm with some pseudocode Python:

```python
def reconstruct_rperfect(M):
    """Given binary matrix M, output an r-perfect phylogeny (if one exists)"""
    k = randomRow(M) # Choose random row of M
    r = state(k) #Get states of row k as a binary string.
    M_prime = flip_cols(M, r) #In all columns i where r(i) = 1, flip the states (0->1, 1->0)
    zero_pp = GusField(M_prime) #Using Gusfield's algorithm, produce 0-perfect phylogeny from M'
    return flip_cols(zero_pp, r) #Flip characters BACK in cols where originally flipped, and return tree.
```

## $r_m$- Perfect Phylogeny

Another theorem is that if $M$ has an $r$-perfect phylogeny for some $r$, then $M$ also has an **$r_m$-perfect phylogeny**: $r_m$ is the **majority string**, where each character of the majority string is the majority of its corresponding column. 

Let us prove this (TODO). 

## Split Equivalence

Our final theorem to prove today is the **split equivalence theorem**: a matrix $M$ has an r-perfect phylogeny iff it satisfies the **four gametes condition**:

For every pair of characters $\chi_i, \chi_j$, one of the following conditions hold:

1. $O_i \cap O_j = \empty$
2.  $O_i \cap N_j = \empty$
3. $N_i \cap O_j = \empty$
4. $N_i \cap N_j = \empty$

Remember that $O_i$ are the set of leaves that possess character $\chi_i$ (formally, all $v$ where $\chi_i'(v)=1$ ) and $N_i = X-O_i$ (all leaves that don't possess the character). 

This is in fact equivalent to stating that one of the character pairs $(\chi_i, \chi_j), (1-\chi_i, 1-\chi_j), (\chi_i, 1-\chi_j), (1-\chi_i, \chi_j)$ are compatible. We'll use this one for proofs. 

What's more, there's *another* way to state this: any character pair $\chi_i, \chi_j$ cannot contain all (four) "gametes": [(0,0), (0,1), (1,0), (1,1)].

Let's prove the myriad of above (equivalent) statements. We'll start with the forward proof: if $M$ has an $r$-perfect phylogeny, then $M$ satisfies the four-gametes condition. 

Again, we define $M'$ by flipping all bits in all columns $i$ where $r(i) = 1$. We know that $M'$ has a zero-root perfect phylogeny: since we know that $M$ has an r-perfect phylogeny, we can simply take *that* tree and flip all columns (characters) where $r(i)$ equals 1 to produce our zero-root. 

Now, consider any $\chi_i, \chi_j$ in $M$, and their counterparts $\chi_i', \chi_j'$ in $M'$, which may or may not have their bits flipped, depending on what $r$ is. **We know $\chi_i', \chi_j'$ are still compatible no matter what, since we know $M'$ has a zero-root perfect phylogeny**. So we again find ourselves with four possible cases: 

1. $r(i) = 0, r(j) = 0$. This means that nothing was flipped and $\chi_i = \chi_i', \chi_j = \chi_j'$. Thus, $\chi_i$ and $\chi_j$ are compatible.
2. $r(i) = 1, r(j) = 0$. This means that $\chi_i' = 1-\chi_i$ (flipped), and $\chi_j$ was untouched. Thus, $\chi_j$ and $1-\chi_i$ are compatible.  
3. $r(i) = 0, r(j) = 1$. This means that $\chi_j' = 1- \chi_j$ (flipped), and $\chi_i$ was untouched. Thus, $\chi_i$ and $1-\chi_j$ are compatible.
4. $r(i) = 1, r(j) = 1$. This means that both characters are flipped: $\chi_j' = 1- \chi_j$ and $\chi_i' = 1-\chi_i$. Thus, $1-\chi_i$ and $1-\chi_j$ are compatible. 

Thus the four gametes condition holds, and we have finished the forward proof.

Now let's grind the backwards proof: if $M$ satisfies the four gametes condition, then it has an $r$-perfect phylogeny. 

Let $r_m$ be the **majority string** of $M$. Then, using that, create $M'$, flipping bits in columns $i$  where $r_m(i) = 1$. We know that $M'$ satisfies the four gametes condition. Additionally, for every character $\chi_i$, we know we have $|O_i| \le n/2$ (the number of objects possessing character $i$ cannot exceed more than half the total objects). 

Additionally, we will assume this following lemma: **a matrix that satisfies the four gametes condition AND satisfies $|O_i| \le n/2$ for every character $\chi_i$ has a zero-root perfect phylogeny**. We can prove this pretty easily through a pairwise compatibility proof.

So because we know $M'$ has a zero-root perfect phylogeny, all we have to do is build that and then flip back the characters on our tree where $r_m(i) = 0$ to produce our lovely r-perfect phylogeny, and we are done!







