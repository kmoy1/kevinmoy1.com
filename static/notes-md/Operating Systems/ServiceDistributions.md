# M/M/1 and M/G/1 Queues

## M/M/1 Queue

In queueing theory, the **M/M/1 queue** is a queue for a single-server system, where **interarrival times **(time between arrivals) have an Poisson distribution, and service times have an exponential distribution. Formally, interarrival times for a process have distribution $\text{Poisson}(\lambda)$, and service times have EXPONENTIAL distribution $\text{Exp}(\mu)$. Here, $\frac{1}{\mu}$ is the **mean service time** (for a request) and $\frac{1}{\lambda}$ is the **mean interarrival time**. 

Given that squared coefficient of variance $C = \frac{\sigma^2}{T_S^2} = 1$, we know our average waiting time (in the **queue**) is given as:

$$T_Q = \frac{\rho}{1-\rho}T_S$$

where $T_S$ is the average service time, and $\rho$ is our utilization, or the arrival rate / service rate. We can see as utilization $\rho$ gets larger (closer to 1), then our waiting time (or **latency**) $T_Q$ explodes. This should make sense: with higher arrival rate, more things have to wait in the queue. 

This is called a **memoryless** service distribution: the system does not remember any arrival history.

## M/G/1 Queue

Here, there are no restrictions on $C$, and it is no longer memoryless. Specifically, service times have a **general distribution**:

$$T_Q = \frac{1+C}{2}\frac{\rho}{1-\rho}T_S$$

