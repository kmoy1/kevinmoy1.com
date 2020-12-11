# Backward Algorithm

As a sort of side-note extension off the Forward Algorithm, the **Backward Algorithm** calculates $b_t(q)$ at each time step, which is the probability of observing $x_{t+1:T}$ given that hidden state at timestep $t$ is $q$:

$b_t(q) = P(x_{t+1:T}|Q_t=q)$ 

To calculate this probability:

$$b_t(q) = P(x_{t+1:T}|Q_t=q) = \sum_{k\in S}a_{qk}e_k(x_{t+1})*b_{t+1}(k)$$

where:

- $a_{qk}$ is the probability that we are in state $k$ (for all possible $k$)
- $e_k(x_{t+1})$ is the probability we emit $x_{t+1}$ at state $q$ (and at timestep $t+1$). 
- $b_{t+1}(k)$ is the probability of observing $x_{i+2:T}$ given that the hidden state at timestep $t+1$ is $k$.

## Application in Likelihood

We can use the above information to calculate the likelihood $P(X|\Theta)$ as:

$$\sum_{k\in S}\pi(k)e_q(x_0)b_0(k)$$

