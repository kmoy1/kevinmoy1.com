# Distributed Transactions

**Distributed transactions** are transactions that access data over multiple *nodes* (separate databases). Let's say we have a database for our company stored in California, one in New York, and one in Shanghai. What if we want to update all three databases with some transaction? This Xact is now *distributed*.  

Another example deals with booking a trip to New York,  which, say, consists of booking a flight, a hotel, a rental car, and a reservation at Per Se. Of course, we want to either book all of these things or book none- it would certainly be a waste of money to book the hotel and reservation but not the flight. 

The ACID properties we know still must be enforced! The most important thing here is the **atomicity**: everything (in different places) are agreeing to either ALL complete the Xact or complete none of it. This has to be synchronized somehow. How? 

Typically, there's a central **coordinator** that ensures all of the Xact is applied to all relevant parts of our units. The most common is the **Two Phase Commit Protocol** (2PC).