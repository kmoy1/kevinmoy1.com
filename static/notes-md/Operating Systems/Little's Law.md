# Little's Law

**Little's Law** is a theorem given by

$$L = \lambda W$$

which states that average number of requests in line at any time $L$ (average length of  a queue) in a system is equal to arrival rate $\lambda$ times average response time $W$ (queue waiting time + service time, or just total time spent in the system). We can also call refer to response time as **latency** for these purposes. This result, amazingly, is independent of the arrival time distribution, the service time distribution, or pretty much anything else.

The only requirement is that system must be **stable**: average arrival rate $\lambda$ is equal to (average) throughput $X$ (requests/s)

## A Basic Example: Taco Truck

Let's look at an example. Let's say there's a taco truck, and on average, the "come and go rate" (arrival rate and throughput, which are equal) is 20 people per hour. Let's also say it takes, on average, 3 minutes for a dude to get their taco after waiting in line. Given this, we can calculate $L$, the number of people waiting at any one time, as: 20/60 * 3 = 1 person. There's always gonna be about 1 person in line at any given time. 

## Another Example

Now imagine a dispensary, with one cashier and a bunch of strains to browse. Let's say arrival rate is equal to exit rate: 20/hr(quick note: a system where arrival rate $\lambda > \mu$ is *unbounded/unstable*, as queue size would $\to \infty$). 

Little's Law tells us the average number of customers in the store, whether browsing or waiting in line or doing whatever, is the arrival rate $\lambda$ times average customer time in store $W$. If potheads arrive at rate $\lambda$ = 10/hr, and stay an average of 0.5 hr, then there are on average 5 potheads in the store (system) at *any* given time!

