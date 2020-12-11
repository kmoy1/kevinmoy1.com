# Byzantine General's Problem

## Overview

The **Byzantine General's problem** is a famous problem in war (and CS!). Let's say France has $n$ leaders for combat: 1 Napoleon Bonaparte (commanding general) and $n-1$ generals. The goal is to coordinate all $n$ generals + their armies to attack **at the same time**: if they can do that, they conquer Spain. Sounds simple enough, right? Here's the catch: among the lieutenants you have a few spies and a couple of dumbasses too. The overarching point: you can't really trust everyone's going to follow the plan. So what do we do here to secure the W? 

We can extend this to any system with some unreliable participants that must agree on a synchronized strategy. For example, let's take a computer, which wants to be able to cope with failure of 1+ of its components (say, the memory corrupts).

## Solution Algorithm

The generals must communicate with each other by messenger (no Zoom or even dinner talk existed back then apparently). For our attack synchronization algorithm, we must guarantee two things:

1. All **loyal** generals must do the same thing- traitor/retarded generals can do whatever. 
2. Traitors cannot cause *defects* from the loyal generals- or deter them from their plan in any way. We'll just assume this is true.

Let's consider how generals reach a decision. Each general scopes target, then communicates his observations to all others. Formally, general $i$ sends $v(i)$ as their report to all $n-1$ other generals. Reports also contain a decision on what to do.  Thus in the end, all $n$ reports $V = \{v(1),...,v(n)\}$ have been collected by *every* general. 

For each general, some arbitrary aggregation method (say, majority vote) is used, and that general votes on their opinion decision. From $n$ decisions, accumulation yet again for the final decision (attack or retreat). Here's the issue: *traitors/retards can send different $v(i)$*: causing conflicts! So for condition 1 to be true, we make an additional assumption that **every loyal general receives the same ** $V = \{v(1),...,v(n)\}$. 

From condition 2, we know MUST prevent a general can use a $v(i)$ that's different from the one sent by general $i$. So we establish another required condition: **if general $i$ is loyal, then his report is received by every LOYAL general as $v(i)$**. In other words, every loyal general uses the same $v(i)$. 

So now, all we have to consider is *how one general sends $v(i)$ to others*. So we can solve the Byzantine Generals' Problem if Napoleon (the commanding general) can send an order to $n-1$ lieutenants, such that no matter what, two **integrity constraints** are fulfilled:

- IC1: All loyal lieutenant generals follow the same order. 
- IC2: If the commanding general is loyal, every loyal lieutenant general obeys every order he sends. (Napoleon CANNOT be assumed loyal)

## Impossibility

The problem is unsolvable if unless more than $\frac{1}{3}$ of the generals are traitors. 