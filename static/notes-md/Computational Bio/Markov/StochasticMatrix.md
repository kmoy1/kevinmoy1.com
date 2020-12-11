# Stochastic Matrix

We know that **stochastic matrices** are directly related with Markov models. But what exactly are they? 

By definition, a stochastic matrix is a matrix that describes the transitions of a Markov chain. For these notes, we usually denote the matrix as $A$, and a specific entry at (i,j) as $a_{ij}$. A stochastic matrix's entries are **transition probabilities**: specifically, $a_{ij}$ is the probability of transitioning from state $i$ to state $j$ for a Markov model. Because these entries are probabilities, a key property of these matrices is that **rows sum to 1**. Columns definitely do NOT have to sum to 1.

We also know that a stochastic matrix must be square: we need one entry per possible pair in $S\times S$. 