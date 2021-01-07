# Baum-Welch Algorithm

The final algorithm learning the parameters of an HMM given an observation sequence $X$. The algorithm will let us train both the transition probabilities $A$ and the emission probabilities $E$ of the HMM.

As a general overview, the BW algorithm computes an initial estimate for probabilities, then build upon those probabilities to make a better set, doing so recursively until we converge on the "best" probabilities. 

Let's consider our ice cream model again. Let's say we know both HOT/COLD classification AND the ice cream count for every day: we are given $Q$ as well as $X$. If we had this, it would be straightforward to calculate HMM parameters $\{\pi, A,E\}$, simply by using **maximum likelihood estimation**. 

Unfortunately, we can only see $X$, not $Q$, in a real HMM. We can't see $Q$ at ALL. This is the heart of the Baum-Welch algorithm: we iteratively *estimate* the counts of each hidden state $s \in S$, for hidden state sequence $Q$.  We *guess* $Q$ and $E$ at the beginning and then use these estimations to make better versions of $Q$ and $E$. 

## Forward-Backward: Recomputing $A$ 

We will need both the **forward probabilities** as well as **backward probabilities** in this algorithm. 

We can estimate our $A$ matrix by estimating $\hat{a_{ij}}$ as **(expected number of $i\to j$ transitions) / (expected number of transitions from state $i$).** 

To compute the numerator, assume we had some estimate of the timestep-specific transition probability $P(Q_{t+1}=j | Q_{t} = i)$. If we had this calculation for *every* timestep $t$, we could simply sum them to estimate $\hat{a_{ij}}$. 

Let's formalize this as $\xi_t(i,j) = P(Q_{t+1}=j, Q_t=i|X,\Theta)$. To compute $\xi_t(i,j)$, we first calculate a probability that's *close* to $\xi_t(i,j)$: 

$$P(Q_{t+1}=j, Q_t=i, X|\Theta) = f_t(i)a_{ij}e_j(x_{t+1})b_{t+1}(j)$$.

We know by the laws of probability that 

$$P(X|Y,Z) = \frac{P(X,Y|Z)}{P(Y|Z)}$$

So we simply need to calculate $P(X|\Theta)$, which we already know as $\sum_{j=1}^{N}f_t(j)b_t(j)$. 

Thus, the final calculation for $\xi_t(i,j)$ is:

 $$\xi_t(i,j) = P(Q_{t+1}=j, Q_t=i|X,\Theta) =\frac{P(Q_{t+1}=j, Q_t=i, X|\Theta)}{P(X|\Theta)} =\frac{f_t(i)a_{ij}e_j(x_{t+1})b_{t+1}(j)}{\sum_{j=1}^{N}f_t(j)b_t(j)}$$

Finally, we can now estimate the numerator of $\hat{a_{ij}}$ (expected number of $i\to j$ transitions) by summing over all $t$ for $\xi_t(i,j)$. The denominator of $\hat{a_{ij}}$ is the expected number of transitions from state $i$ just extends that summation by summing over all possible $j$, then $t$. Therefore:

$$\hat{a_{ij}} = \frac{\sum_{t=1}^{T-1}\xi_t(i,j)}{\sum_{t=1}^{T-1}\sum_{k=1}^{N}\xi_t(i,k)}$$

## Forward-Backward: Recomputing $E$

To recompute emission probability matrix $E$, we need a way to calculate our estimation $\hat{e_j}(x_k)$. We can estimate this as  **(expected number of times in state $i$ while observing  $x_k$ ) / (expected number of times in state $j$)**. 

To calculate the numerator (expected number of times in state $i$ while observing $x_k$), we first calculate the probability of being at (hidden) state $j$ at timestep $t$: 

$$\gamma_t(j) = P(Q_t = j | X,\Theta)$$

which by Bayes' rule we can reduce to: 

$$\gamma_t(j) = \frac{P(Q_t = j, X|\Theta)}{P(X|\Theta)}$$

Hey! We already know how to compute both the numerator AND denominator, so we can simplify this further as

$$\gamma_t(j) = \frac{f_t(j)b_t(j)}{P(X|\Theta)}$$

Thus to calculate the expected number of times in state $i$ with observation $x_k$, For the numerator, we sum $\gamma_t(j)$ for all timesteps $t$, *under the condition that we observe $x_k$ at that timestep*. The denominator is much simpler than the transition matrix: the expected number of times in state $j$ is simply the sum of $\gamma_t(j)$ over all ($T$) timesteps. Therefore, our final estimation for $E$ is given as: 

$$\hat{e_j}(x_k) = \frac{\sum_{t=1, \text{s.t.}X_t=x_k}^{T}\gamma_t(j)}{\sum_{t=1}^{T}\gamma_t(j)}$$

## Putting it Together

Finally, we know how to estimate transition matrix $A$ and emission probabilities $E$ given an observation sequence $X$. First there is an **initialization** stage, where we make initial estimations of $A$ and $E$. 

We then go into iteration, and split up each iteration into two steps, **expectation** and **maximization**:

- Expectation: calculate $\gamma_t(j)$ and $\xi_t(i,j)$ for all possible hidden states $i,j$ and all timesteps $t$. 
- Maximization: from the two expectation terms, we calculate our estimations of $A$ and $E$ as $\hat{a}_{ij}$ and $e_j(x_k)$ 

  We iteratively run through these steps until our estimations converge. By "converge" I mean the change in likelihood probability $P(X|\Theta)$  after an iteration goes under a certain threshold: these become our "official" estimates.

## Pseudocode

Let's run through our Pseudocode for Baum-Welch in Python:

```Python
def BaumWelch(O, Sigma, Q)
	"""Given observation sequence O and state + emission spaces, return a model HMM.""""
	A, B = initialize()
```



