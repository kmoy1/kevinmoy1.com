# Forward Algorithm: Likelihood

One thing that can be derived from HMMs is calculating the likelihood of a particular observation sequence. Specifically, given observation sequence $X$ and HMM $\Theta$, what is $P(X|\Theta)$?

For Markov chains, this is easy, as there's only one observable state: none of this "hidden" vs, "observable" BS. In that case, given a sequence $X = \{X_1,...X_n\}$, our probability would just be $\pi_{X_1}P(X_2|X_1)...P(X_n|X_{n-1})$. Unfortunately, it's a little more complex here: we don't know what the hidden states are! We just know observations ("emissions"). 

Let's review our ice cream model again. Remember there are two hidden states S = {"HOT", "COLD") and 3 emissions $\Sigma=${1,2,3}. Let's say we want to predict the probability of a sequence like $X=\{3,1,3\}$: in other words, we observe 3, 1, 3 in 3 time steps. This is all we *can* observe.

Before we predict that, though, let's start with something simpler. Let's say given our *hidden* states at each timestep as S = {H,H,C}, it is much easier to calculate the probability of emission sequence $X=\{3,1,3\}$. We know there's a 1-to-1 correspondence between an emission and a state. Thus it's just $P(X_3=3|Q_3 = C)P(X_2=1|Q_2=H)P(X_1=3|Q_1=H)$ = 0.1 * 0.2 * 0.4 = 0.008. (NOTE: For future probabilities, we will represent this as $P(313|HHC)$).

Generally, given a hidden state sequence $Q$ of length $T$, the probability of a (length-$T$) emission sequence is straightforward:

$$P(X|Q) = \prod_{i=1}^{T}P(x_i|q_i)$$

But again, we don't know this hidden state sequence. So instead we **marginalize over $Q$**. We know there are 8 possible sequences for $Q$. Thus, our probability $P(X)$ can be given as:

$$P(X) = \sum_{Q}P(X,Q) = \sum_{Q}P(X|Q)P(Q)$$ 

Generally, given $T$ observations and $N$ hidden states, there are $N^T$ possible corresponding hidden state sequences corresponding to the observations. This is an **exponential number** of possibilities. Not good. So we need another way. 

## The Forward Algorithm

We can reduce runtime from $O(N^T)$ to $O(N^2T)$ with the **forward algorithm**, an algorithm that utilizes dynamic programming. 

The forward algorithm computes our marginalized observation probability **efficiently**. How? Given an observation sequence $X$, we can create a **forward trellis**, which is a graph representing possibilities of hidden states and transitions as time goes on:

![image-20201206181851037](C:\Users\Kevin\AppData\Roaming\Typora\typora-user-images\image-20201206181851037.png)

We can calculate each **trellis cell** $\alpha_t(j)$ (some notations label this as $f_t(j)$, which is the probability of being in (hidden) state $j$ at time step $t$, as well as emitting $X_t$. We look at all paths that can lead to state $j$ and sum them up: 

$$\alpha_t(j) = f_t(j) = P(x_{1:t},Q_t=j|\Theta)$$

For a given state $Q_j$ at time step $t$, our trellis cell $a_t(j)$ is computed as:

$$\alpha_t(j) = e_j(X_t)\sum_{i=1}^{N}\alpha_{t-1}(i)\alpha_{ij}$$

where:

- $\alpha_{t-1}(i)$ is the **previous forward path probability** from the previous time step: the probability of hitting the cell at the *previous* trellis cell.
- $a_{ij}$ is the **transition probability** from state $i$ to state $j$. 
- $e_q(X_t)$ (alternately written as a matrix term $e_{qi}$)  is  the **emission probability** of emitting observation $X_t$ (at time step $t$) while at hidden state $q$ (at time step $t$).
- $i$ is the $i$-th (enumerated) hidden states out of $N$ possible.

So we can see each term in the summation represents one of the $N$ possible ways to reach a hidden state and then, from that point, transition onto our current hidden state and emit our observation. 

Let's take a look at an example. Let's say for our ice cream model, given **partial observation sequence** {3,1}, we want to calculate the forward probability of $Q_2 = H$. In trellis cell terms, we want to calculate $\alpha_2(H)$.  There are two possible trellis paths: HH and CH. We simply add their probabilities below:

$$\alpha_2(H) = \alpha_1(H)P(H|H)P(X_2 = 1|H) + \alpha_1(C)P(H|C)P(X_2 = 1|H)$$

## Another Visualization

We can also think of the formula for $\alpha_t(i)$ as the sum of all (possible) previous values $\alpha_{t-1}$, *weighted by transition probabilities $a$*, and multiplying the summation by emission probability $e_i(X_t)$. Let's consider another visualization:

![image-20201206220012659](C:\Users\Kevin\AppData\Roaming\Typora\typora-user-images\image-20201206220012659.png)

Notice that time step $t$ (with known observation $o_t$) is the only step we really care about. Because of the Markov property, $\alpha_t(j)$ is only dependent on time step $t-1$. Hidden state $i$ at time step $t$ is denoted by $q_t(i)$ and are circle nodes. 

## Algorithm

Now, let's write out the forward algorithm in Python pseudocode:

```Python
def Forward(O, Theta):
    """Given T observations in O, as well as model THETA, calculate forward probability for STATE at timestep T."""
    S, A, E, pi = getModelParams(Theta) #Get hidden state space, observation space, transition matrix, EP, start
    T = len(O)
    N = len(S)
    DP = createDP(N, T) #Create NxT DP table for forward probabilities a_t(i)
    #Initialization
    for s in S:
        DP[s, 1] = pi(s) * E(s, O[1]) #first observation O[1], or O[0] if you want.
    #Recursion
    for t in range(2, T):
        for s in S:
            total = 0
            for s_prev in S:
                total += DP[s_prev, t-1] * A[s_prev, s] * E(s, O[t]) #The forward trellis algorithm
            DP[s, t] = total
    #Termination: return our forward probability. 
    return sum([DP[s, T] for s in S])
```

We know we are given an set of $T$ observations $X$, as well as our HMM $\Theta$, and want to calculate **likelihood**  $P(X|\Theta)$. 

Let's break down each of the initialization, recursion, and termination steps. First, in initialization, we establish the very first trellis cell $\alpha_1(j)$: at timestep 1 (initialization), we calculate the initial forward probability of each possible hidden state $j \in S$: 

$$\alpha_1(j) = \pi_je_j(X_1)$$

Simple enough. This initialization calculation allows us to use dynamic programming in the recursion phase to calculate next-level forward probabilities via:

$$\alpha_t(j) = \sum_{i=1}^{N}\alpha_{t-1}(j)a_{ij}e_j(X_t)$$

again calculating $\alpha_t(j)$ for each state $j \in S$. We also repeat this calculation for every timestep $1 < t \le T$. 

Finally, to calculate $P(X|\Theta)$ in the termination phase, we simply sum ALL $N$ forward probabilities calculated for the previous timestep $t-1$: 

$$P(X|\Theta) = \sum_{i=1}^{N}\alpha_{T}(i)$$

And we are done.

