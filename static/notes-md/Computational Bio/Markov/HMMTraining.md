# Training a Hidden Markov Model

Remember that Hidden Markov Models are all about models with a state sequence that *we do not see* - and what questions we could answer from it. The main three questions to answer were *likelihood estimation*, *decoding*, and *model learning*. Model learning in particular is generally considered to be the most difficult: we only have the observation sequence, and *not the model*. 

Let's think about a model with a cheating casino (or "casino", for short), with a dice game that rolls 1-5 with probability $\alpha/5$ for some arbitrary $\alpha$, and 6 with probability $1-\alpha$. **But we don't know this**. All that we have are these recorded rolls:

```25111351331524253316655632235542541666```

We want to derive the model $\Theta$ from these observations. Specifically, we want a *very good estimate* of transition matrix $A$, the emission probability matrix $E$, and the initial distribution $\pi$. We can actually write this as a probability:

$$\underset{\Theta}{\operatorname{argmax}}P(X|\Theta)$$

which just means we want the model $\Theta$ that maximizes the probability that it produces the observations we see. 

This is a complicated problem. To ease into this, we'll start off by assuming we *do* know the hidden state sequence, and see if we can generalize from there. 

## Training a Model: Our Goal

What does it mean to "train" a HMM? We are really just finding the optimal set of parameters that make the model. Generalizing a model given a set of observations comprises the broad and exciting area of **supervised learning**- although that topic is for another note. 

The **hyperparameters** we do know about the model are the observations $X$, as well as the hidden state space $S$. 

We usually have many **iterations** of observation sequences. Let's say we have 500 iterations of 1000 die rolls. The 500000 resulting observations makes our training set. We can denote the $k$-th iteration of observations as $I^{(k)}$. For our current example, we therefore have iterations $I^{(0)}$ to $I^{(499)}$- 500 iterations total. Now, specific observations look like $i_l^{(k)}$, where it is the value of the $l$-th observation in iteration $k$. 

So the goal is to use this training set to get a pretty good idea of what our model would look like. Formally, we want to find 

$$\underset{\Theta}{\operatorname{argmax}}P(I^{(0)}...I^{(n)}|\Theta) = \underset{\Theta}{\operatorname{argmax}}\prod_{d=0}^{n}P(I^{(d)}|\Theta)$$ 

for $n$ iterations in our training set. Obviously, the probability of each iteration is independent, since we reset the HMM each time. 

## Take 1: We know the hidden state sequence

Let's say for our casino model, we know the corresponding hidden state for each observation (which die is chosen on each roll). Formally, we now have observations $q_{1:L}^{(0)}, q_{1:L}^{(1)},...,q_{1:L}^{(n)}$ for $n$ iterations and $L$ observations per iteration. We'll just assume we know the length and denote these observation iterations as $q^{(0)},...q^{(n)}$ for now. 

Given this, we want to find the **maximum likelihood estimate** for our parameters: $a_{ij}$, $e_k(i)$, $\pi$. Without proof, the MLE for our HMM parameters are:

$$\hat{a}_{k,q} = \frac{A_{k,q}}{\sum_{q'\in S}A_{k,q'}}$$

$$\hat{e}_{k,i} = \frac{E_{k,i}}{\sum_{i'\in S}E_{k,i'}}$$

$$\hat{\pi}_{k} = \frac{\Pi_{k}}{\sum_{q'\in S}\Pi_{q'}}$$

where: 

- $A_{k,q}$ is the number of transitions from hidden state $k$ to $q$ in our hidden state sequences.
- $E_{k,i}$ is the number of times character $i$ was output on hidden state $k$. 
- $\Pi_k$ is the number of iterations where state $k$ was first (NOTE: we should have sufficient iterations)

## Take 2: We don't know the hidden state sequence 

Now that we know how to estimate our HMM $\Theta$ given *both* our observation sequence(s) and hidden state sequence(s). Can we possibly *still* get a good estimate of $\Theta$? Remember our goal: finding $\underset{\Theta}{\operatorname{argmax}}\prod_{d=0}^{n}P(I^{(d)}|\Theta)$

SIDENOTE: the more parameters we have, the more the likelihood (of the model) is going to improve- but the complexity increases as well. 

Let's grind into an algorithm known as the **Baum-Welch algorithm** or colloquially as the **Forward-Backward algorithm** (as it utilizes BOTH forward probabilities $f_t(i)$ as well as backward probabilities $b_t(i)$). The basic idea is that we are iteratively cycling between **parameter estimates** and an evaluation of those estimates based on the most likely hidden states that we produce. On each iteration, we are tuning the parameter estimates until convergence. 

We need to initialize $\Theta$: we can *do so randomly*, and hope we don't converge on some bullshit (a local extremum). Given our observations, we want a way to measure **expected frequencies** $A_{kl}$, $E_k(i)$,$\Pi_k$. In the maximization phase, we assume our expected frequencies are correct, and use it to produce the MLE of our parameters: $a_{kq}, e_q(i), \pi_k$.

Bonus: **Likelihood is guaranteed to increase after each iteration**. We terminate only when this increase gets close enough to 0 (s.t. we can say we converge). 

## Baum-Welch Algorithm

Let's say we have $n$ sets (iterations) of observations, labeled $I^{(1)},...,I^{(n)}$. Each set has $L$ observations, denoted $i_1,...,i_L$. We also know how many hidden states we have. 

Given the above inputs, we want to output the maximum likelihood estimate (or inference) of the "true" model: we want to estimate $\Theta = \{a_{kq}, e_k(i), \pi_k\}$. 

The first thing we do is initialize $\Theta$ as $\Theta_0$: we can do this randomly. 

Next, we compute the **likelihood** for our random data $L^0 = P(I|\Theta_0)$.  This likelihood should be *shit*, and that's okay! We already know how to utilize the Forward algorithm for this. 

Then, we enter a loop. We start with the **expectation step (E step)**: utilizing the $\Theta_j$ from the previous iteration, we compute expectations $E_k(i)$, $A_{kl}$, and $\Pi_k$, which are just *expectations* of their lowercase-level counterparts. We know how to do this above in Take 1! After the E step, we enter the second stage: the **M step** (maximum likelihood calculation step). In the M step, we update $\Theta_{t-1}$ to $\Theta_t$, according to the *maximum likelihood*. Remember how we calculate our updated parameter estimations from our expectations:

$$\hat{a}_{k,q} = \frac{A_{k,q}}{\sum_{q'\in S}A_{k,q'}}$$

$$\hat{e}_{k,i} = \frac{E_{k,i}}{\sum_{i'\in S}E_{k,i'}}$$

$$\hat{\pi}_{k} = \frac{\Pi_{k}}{\sum_{q'\in S}\Pi_{q'}}$$

From these updated parameters, we calculate an updated likelihood $L^t = P(I|\Theta^t)$. When the difference between the likelihoods is small enough, we terminate, and return $\Theta^t$. 

So we already know how to do the M step. But how do we do the E step??

## E Step: Making expectations given $\Theta$

### Estimating $\Pi_k$

Let's first find a way to estimate $\Pi_k$. Remember that $\Pi_k$ is the *expected* number of initializations at hidden state $k$ (from all iterations). Formally, we can write $\Pi_k$ as:

$$\Pi_k = P_\Theta(Q_1=k|x_{1:L})$$

Let's start with how to calculate $\Pi_k$ for ONE iteration.  We know how to reduce this: we've seen the above formula in decoding!

$$\Pi_k = P_\Theta(Q_0=k|x_{1:L}) = \frac{P_\Theta(Q_0=k, x_{1:L})}{P_\Theta(x_{1:L})}$$

We know the denominator is just the sum of all forward probabilities on the last timestep:  $\sum_{q\in S}f_L(q)$

What about the numerator? We also know this from posterior decoding! We know $P_\Theta(Q_t=k, x_{1:L})$ is simply $f_t(k)b_t(k)$. 

Thus we can reduce $\Pi_k$'s formula to:

$$\Pi_k = \frac{f_0(k)b_0(k)}{\sum_{q \in S}f_L(q)}$$

Thus to get the new $\Pi_k$ over all iterations, we simply sum over all observation sequences: 

$$\Pi_k = \sum_{d=0}^{n}\frac{f_0^{(d)}(k)b_0^{(d)}(k)}{\sum_{q \in S}f_L^{(d)}(q)}$$

### Estimating $E_k(i)$

We can calculate $E_k(i)$ in a similar fashion: just sum the probabilities that state $k$ is a hidden state *over all instances* where $i$ is observed.

Let's say observations $I^{(0)} =\{6,1,2,6,4\}$. We know our two states are {L,F}: loaded or fair die used. Then $E_F(6)$ would be the expected number of times the outcome was 6 given we were at hidden state F: in other words, the number of times a fair die rolled 6. We know 6 is output at timestep 0 and timestep 3. Thus we can represent $E_F(6)$ as the probability that the hidden states at steps 0 and 3 are F:

$$P(Q_0 = F | I) + P(Q_3 = F | I) = \sum_{t|i_t=6}P(Q_t=F|I)$$

And we already know that $P(Q_t=k|I)$ is our posterior decoding term we discussed above! Thus we simply sum to get:

$$E_k(i) = \sum_{t|i_t=i}\frac{f_t(k)b_t(k)}{\sum_{q \in S}f_L(q)}$$

which means we ONLY add terms from timesteps where the emission in question ($i$) actually occurred.  

### Estimating $A_{kl}$

This is just a variation on the previous calculation: we sum ALL $k \to l$ probabilities (over all observations). Here's the problem, once again: **we don't have any hidden state information**. To make up for this, we simply **marginalize over all possible timestep transitions**: one from t = 0 to t = 1, another for t=1 to t=2, all the way up to t = L-1 to t = L. Thus for our above example with one iteration, with $I^{(0)} =\{6,1,2,6,4\}$, we estimate $A_{FL}$ (expected number of transitions from F to L) as:

$$P(Q_0=F,Q_1 = L|X) + P(Q_1=F,Q_2 = L|X) +P(Q_2=F,Q_3 = L|X) +P(Q_3=F,Q_4 = L|X)$$

which can be further generalized as:

$$\sum_{t=0}^{D-1}P(Q_t = F, Q_{t+1} = L|I^{(0)})$$

Pay attention to the summation limit: given an observation sequence with $D$ observations, there are only $D-1$ transitions we care about!

How can we calculate $P(Q_t = F, Q_{t+1} = L|X)$? Well, let's just display our generalized formula now without proof:

$$P(Q_t = k, Q_{t+1} = q|X) = f_t(k)a_{kq}b_{t+1}(q)e_q(i_{t+1})$$

Let's run through the 4 product terms:

- $f_t(k)$ is the probability of $Q_t = k$ given all our observations before step $t$.
- $a_{kq}$ is the probability of transitioning from state $k$ to $q$. 
- $e_q(i_{t+1})$ is the probability of emitting observation $i_{t+1}$ at state $q$. 
- $b_{t+1}(q)$ is the probability of $Q_{t+1}=q$ given that we observe what we do from timestep $t+1$ to the end.

Since all four need to "occur" for our desired probability event, the product should now make sense!

Thus we can now finally write out our expectation of our transition matrix as

$$A_{kq} = \frac{f_t(k)a_{kq}b_{t+1}(q)e_q(i_{t+1})}{\sum_{q\in S}f_L(q)}$$

And we are done! We know how to do the E step and M step in full, as well as know how to calculate our given likelihoods. 





