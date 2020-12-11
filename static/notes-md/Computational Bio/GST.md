# Generalized Suffix Trees

We know we can build a suffix tree for a string in linear time. However, what if we wanted to build a tree for *multiple* strings, say, a set of $z$ strings $\{S_1, S_2,...,S_z\}$? 

This is where **generalized suffix trees** (GSTs) come into action, which are in reality just a basic extension of suffix trees! Let's take a look how.

## Building a GST

How do we build a GST? An easy way is to just concatenate each string together, but separating them by a different terminator character (one that's not in any of the strings). For example, if our string set is {'apple', 'pear', 'orange'}, we would simply create a suffix tree for 'apple\$pear#orange@'. Building our suffix tree from this takes runtime equal to the sum of all strings in the set. Leaves in a GST are actually a **pair of numbers (i,j)**: where $i$ identifies string $S_i$ and $j$ represents the index in $S_i$ that contains the substring.

While this does work, it's not very ideal. The tree will contain many *overlapping substrings*- that is, substrings of the concatenated string that span more than one string. In our above example with the suffix tree for 'apple\$pear#orange@', we certainly have no use for a substring like 'le\$pear#or'. Ideally, NONE of our substrings contain delimiter characters! So usually, our GST is truncated at the delimiter character.

## Applications

The GST's inherent structure allows us to find the **longest common prefix** among all pairs of suffixes from a pair of strings $S_1$ and $S_2$. 