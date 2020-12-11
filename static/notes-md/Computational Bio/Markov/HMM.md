Remember that a **Markov Model** is characterized by a random variable $Q_t$, representing the state at timestep $t$, transition probability matrix $A$, and initial probability distribution $\pi$. 

A **hidden Markov model ** is an extension of Markov chains where states $Q_t$ are now treated as **unobservable/hidden states**. The states we *do* see are called **emissions**, represented by $x_t$ at time step $t$. $Q_t$ can represent anything that's done "behind-the-scenes": for example, a cheating casino switching to loaded dice every time step with some chance. 

An HMM is characterized by a triplet $(\Sigma, S, \Theta)$:

- $\Sigma$ is the set of all possible emissions (all possible observations)
- $S$ is the set of all possible hidden states.
- $\Theta$: Model, represented by three parameters: 
  - Initial state probabilities $\pi$
  - Transition probability matrix for hidden states $A$, where $a_{ij}$ = $P(Q_{t+1} = j | Q_t = i)$ 
  - Emission probability/observation likelihoods $e_{qi}$ OR $e_q(i)$, which is the probability of emitting observation $i$ at (hidden) state $q$.

Hidden Markov models implement the **Markov property**, which states that $P(q_i | q_{i-1}, q_{i-2},...,q_1) = P(q_i | q_i-1)$ . In other words, future states only depend on current state- the state immediately before it. 

Another important property that HMMs implement is that of **output independence**: the probability of observing output $x_i$ ONLY depends  on the hidden state that produced that output, and NOTHING else: $P(x_i|q_1,...,q_T,o_1,...,o_T) = P(x_i|q_i)$ (for $T$ observations).

That's a mouthful so far, so let's consider an example. 

Imagine you are in the year 3000, studying global warming's history. Records from 2020 about weather were all burned in World War III, so you have to find another means to study weather. You find Joe Smith's journal- which contains info on how much ice cream he ate daily back in 2020. So here's the big question: *can we use fat Joe's notebook to estimate daily temperatures in 2020?* 

Given a sequence of observations $X = \{x_1, x_2,...x_n\}$, where $x_i$ = number of ice creams Joe ate on day $i$, we want to find the **corresponding hidden state sequence**. In particular, we want to find out if each day was hot (H) or cold (C) (a gross simplification that we can expand on later). Since we don't actually know, H and C are **hidden states**! 

Let $\Sigma$ = $\{1,2,3\}$, and $S$= $\{H,C\}$. We can then design our HMM as such:

![image-20201130224746938](C:\Users\Kevin\AppData\Roaming\Typora\typora-user-images\image-20201130224746938.png)

## Three Fundamental Questions in Markov Learning

There are three fundamental questions that characterize Hidden Markov Models:

1. **Likelihood**: Given an HMM $\Theta$ and observations $X$, calculate likelihood $P(X|\Theta)$.
2. **Decoding**: Given observations $X$ and HMM $\Theta$, we want the most likely ("best") **hidden state sequence** $Q$. 
3. **Learning**: Given observations $X$ and states $Q$, learn "best" model $\Theta$. 

