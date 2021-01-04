# Felsenstein's Algorithm: Estimating Phylogenetic Likelihood

Given a character $\chi$, a rooted phylogenetic tree $T$, and transition probabilities $P$ (state transition) and $\pi$ (initial probabilities), we want to calculate the **likelihood of tree $T$**: formally, we want to calculate $P(\chi|T)$. 

We can express this naively as $P(\chi|T) = \sum_{\chi'}P(\chi'|T)$ where $\chi'$ are all the character extensions. 

Let's dive into the algorithm, which makes use of a very familiar dynamic programming structure

First, we define $q(v,s)$ which represents the likelihood of the tree rooted at $v$ given that the state of $v$ is (set to) $s$. We know this is equal to $P(\chi|T, \text{state}(v) = s)$. 

Now here's the DP step: we take the probability of marginalizing over BOTH the left and right subtrees. Thus $q(v,s)$ is equal to

$$\sum_{s_L \in S} P(\chi, \text{state}(L) = s_L | T, \text{state}(v)=s) * \sum_{s_R \in S} P(\chi, \text{state}(R) = s_R | T, \text{state}(v)=s)$$

where $L, R$ are the left and right child nodes of $v$, and $S$ are our possible tree states (ATCG). 

We can reduce this further to 

$$\sum_{s_L \in S} P_{s,s_L}q(L,s_L) * \sum_{s_R \in S} P_{s,s_R}q(R,s_R)$$

Specifically, we are calculating the sum of probabilities of all possible state assignments to $L(v)$, where each term is the transition from state $s$ (at $v$) to that state assignment ($s_L$), and then the likelihood of the (left) subtree rooted at $L(v)$ given that the state assignment is that node ($s_L$). We repeat this for the right subtree and multiply the two probabilities together. 

