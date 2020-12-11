# End-to-End Principle

The **end-to-end principle** is a design pattern for computer networks that put **all application-specific features at endpoints** of a network connection instead of in the middle. The network should *only* be responsible for providing a secure and reliable connection, and *absolutely nothing else*. 

One of the basic premises of this design is that adding features to our network quickly diminish. When such a feature is purely for spec-related reasons for a very specific connection, there is usually VERY little reason to generalize this to the network layer, and start to fuck with ALL connections.

Let's say process A and process B are in communication through some transport layer medium. Since reliability needs to be implemented at the application layer (the processes) anyway, there's no need to implement reliability in the *intermediary nodes*: the nodes that make up the transport medium. 

We know that the **Internet Protocol** (IP) makes *no delivery guarantees*. The **Transmission Control Protocol** (TCP) is responsible for handling those guarantees, via e2e acknowledgement and retransmission of lost/corrupted packets. 