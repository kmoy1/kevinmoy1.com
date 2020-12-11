# Viterbi Algorithm

One of the three essential questions one can ask from a Hidden Markov Model is **decoding**: given an observation set $X$ and HMM $\Theta$, **what is the best hidden state sequence** $Q$? We can represent this as $\underset{Q}{\arg\max}P(Q|X,\Theta)$. 

This is a little more complex. Again, the naive solution might be running through each possible hidden state sequence $q$ and run the forward algorithm and computing $P(X|q)$, and choose the HSS $q$ that maximizes $P(X|q)$. But again, runtime shit. 

So a better decoding algorithm we're going to learn about is the **Viterbi Algorithm**. Like the forward algorithm, Viterbi utilizes DP heavily. If you have any experience with dynamic programming using *minimum edit distance*, you'll find that the Viterbi algorithm is *very* similar. 

Let's say we want to compute the best $q$ for observation sequence X={3,1,3}. The diagram below shows how it's done:

![image-20201206233432709](C:\Users\Kevin\AppData\Roaming\Typora\typora-user-images\image-20201206233432709.png)

We want to go left to right and calculate each cell of the trellis as $v_t(j)$, which represents the probability that we are in hidden state $j$ **given we have seen the first $t$ observations $x_{1:t}$** as well as $t-1$ *previous* hidden state steps $q_1,...,q_{t-1}$. 

Formally, each cell expresses probability

$$v_t(j) = \max_{q_{1:t-1}}P(q_{1:t-1},x_{1:t}, q_t=j|\Theta)$$

Our cell value is thus computed by **recursively taking the most probable path to the cell**. We represent "most probable path" as the maximum over *all possible hidden state sequences* $q_{1:t-1}$. 

Again, this sounds like a job for DP! Given that we computed the probability of being in every state at time $t-1$ ($v_{t-1}(j)$ for every $j\in S$), we can compute the Viterbi probability by simply calculating the most probable extension of the path that leads to the current cell. 

For a given hidden state $j$ at time $t$ (as well as observation $X_t$), we simply calculate $v_t(j)$ by running through all possible states and taking the max of extensions:

$$v_t(j) = \max_{i=1}^{N}v_{t-1}(i)a_{ij}e_j(X_t)$$

which should be pretty similar to the Forward algorithm, except since we only want ONE path probability (the most likely one), we take a maximum instead of summing over everything possible. We call $v_{t-1}(i)$ the **previous Viterbi path probability** from (previous) time step $t-1$, and transition + emission probabilities remain the same as before in the Forward algorithm.

## Viterbi Algorithm: Code

Let's establish some Python pseudocode for the Viterbi algorithm. This time, instead of just returning a single probability, we want not only our maximal HSS's likelihood but also the maximal HSS itself! So our algorithm is considerably more complex:

```python
def Viterbi(O, Theta):
    """Given observations O and model THETA, return most likely HSS + its probability."""
    S, X, A, E, pi = getModelParams(Theta)
    T = len(O)
    N = len(S)
    DP = createDP(N, T) #Create NxT DP table for viterbi path probabilities v_t(i)
    #Initialization
    for s in S:
        DP[s,1] = pi(s) * E(s,O[1])
        BP[s,1] = 0 #Backpointers so we can recover HSS.
    #Recursion
    for t in range(2, T): #We can skip first observation.
        for s in S:
            DP[s,t] = max([(lambda s2: DP[s2,t-1]*A(s2,s)*E(s,O[t]))(x) for x in range(1,N)]) #Save prob
            BP[s,t] = argmax([(lambda s2: DP[s2,t-1]*A(s2,s)*E(s,O[t]))(x) for x in range(1,N)])
    #Termination
    best_path_prob = max([DP[s,T] for s in S])
    best_path_pointer = argmax([DP[s,T] for s in S], key=s)
    best_path = backtrace(BP, best_path_pointer)
    return best_path, best_path_prob
```

Notice the introduction of another DP table: **backpointers**, to store our most likely hidden state sequence and backtrace when we reach the end to get our sequence! We call this HSS found by the **Viterbi backtrace**. 

Let's wrap this up by formalizing the Viterbi algorithm, again via the familiar initialization, recursion, and termination steps. 