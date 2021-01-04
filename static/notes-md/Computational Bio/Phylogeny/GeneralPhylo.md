# General Phylogenetic Reconstruction

Now, given a set of nontrivial characters $\chi_1,...,\chi_d$, we want to find a phylogenetic tree $T$ that **minimizes the number of changes**. We still assume binary characters, but now **the tree no longer has to be rooted**. Incredibly scary. 

Now we delve into the realm of graph theory. If we have $d$ characters, then we know we have $2^d$ possible states. We'll construct a graph $G$ that correspond to these states:

$$G = (V, E, w)$$

- $V = \{0,1\}^d$ ($d$ binary vertices)
- $E = \{(u,v) | \text{Hamming}(u,v) = 1\}$ (node pairs with Hamming distance = 1). Edges connect vertices that differ by ONE mutation.
- $w(u,v) = 1$: edge weights are always 1.

We use **Steiner's tree problem** and **hypercubes** in this case. 

