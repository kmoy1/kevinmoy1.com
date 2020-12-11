# Two Phase Commit 

The **Two Phase Commit** protocol is an algorithm that coordinates processes in a distributed transaction. Specifically, each participant process either **commits** their change or **aborts** (rolls back) their change. For recovery upon failure/error, log records for each machine are used. 

Assuming no errors occur, 2PC has two main phases. 

## Stage 1: Prepare Phase

Also called the **commit-request phase** or the **voting phase**, in this stage the coordinator asks all participant processes (also called *workers* or simply *nodes*) to choose between committing or aborting the given Xact. Then, each participant does three things, depending on what choice they make:

1. *Prepare* to commit/abort. Usually, the participant executes the Xact *locally*, and if everything passes, they choose commit, but if it doesn't, then abort.
2. Vote to commit with "Yes" or "VOTE-COMMIT", or to abort with "No" or "VOTE-ABORT". Vote sent to coordinator.
3. **Log** their vote.

## Stage 2: Commit Phase

Once the coordinator has all the participant's votes, the coordinator will decide the "official" or "global" commit/abort. ***A global commit is made only if all participants vote yes*:** if there's even one participant "VOTE-ABORT", then it's an global abort. 

The coordinator logs the global decision, then broadcasts it to all the participant nodes. The participants then execute the official Xact decision and, when done, send an ACK to the coordinator. Once the coordinator receives ACKs from all participants, it logs "Got Commit", and we are done. 

## Logging

Each machine/process also keeps a **log** to track whether they committed an Xact or not. These are utilized in recovery procedures. For example, if a participant machine crashes, when it reboots it immediately checks log to restore its state at the time of crash. 

Each participant machine/process specifically has a **write-ahead log**, a special means of logging such that atomicity and durability are ensured. In WAL, any Xact changes are first logged and saved in **stable storage** before the Xact is actually carried out. This makes the recovery process consistent, as intended changes are always saved before they are carried out, so we have a roadmap on what to do.  

