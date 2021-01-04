# BWT 1: Introduction

A wonder of the English language is *anagrams*: a sequence of letters that can be rearranged into multiple things. For example, let's say we have sequence ENTSLI. Do we rearrange this to LISTEN? Or SILENT? Or TENSIL? 

We can actually generalize anagrams to the **Burrows-Wheeler Transform** (BWT) of a string: we *permute* (shuffle around) the letters in a string to not only make compression easier but also process it to make other string tasks easier. But even though the number of permutations for a document become large *very* quickly, BWT actually makes it fairly simple and quick to find the "correct" origin word!

Let's focus on the first purpose of BWT: compression. A common theme in BWTs are that characters are often in **runs**. A common example is this "BWT excerpt" from the BWT on Shakespeare's *Hamlet*:

`nnnnnnnnnnnnnnnnnntnnnnnnnhnnngnnnnnnnnjnnnnnhdnnng nnnnonnNnnnhhNnnnnnnnnntnnhnnnnnnnnnnnnnnNnndnnnhnn nnnNnnnnnnnnnnnnnnnnnnnnnonntnnNNnnnnnnnndngnnnnnnn nnnnnnnNnnnnnnnngnnnnnnnnnnnnnnnnnngnnnnnnnnonnnnnn nnnNNnlnnnhnnnnnnnnnntdbdnnrrmnnmnmnnnuoccppppppdnr rDolBbbdddodbbBddbbddbdBdbbdbdDddddBbbbbdDbubbdbdbB`

Notice that there's a TON of `n` runs in this string, and the above can easily be compressed to a string where the number of contiguous occurrences precedes the character: 

`19nt7nh3ng8nj5nhd3ng`

This is just intuition: in real life, BWT is more sophisticated in order to exploit other characteristics of the string. But the encoding part of BWT is simple, fast, and allows **lossless compression** (compression that doesn't lose any data). 

Enough talk: let's get into how it works. 

## BWT Transformation

Whenever we mention BWT, we are talking about the *BWT transform on some string*. Let's say our string $S$ is "barbara\$" (sentinel always added, but it's actually not always necessary in this case). We want the BWT of this string:$BWT(S)$.

The first step is to **list all possible rotations of our string**. We can just consistently rotate a character from the beginning to the end and note that down until we get all rotations. So for string "barbara$", with 8 characters we'd have a **BWT matrix** consisting of 8 rotations of the string:

```
                                                    barbara$
                                                    arbara$b
                                                    rbara$ba
                                                    bara$bar
                                                    ara$barb
                                                    ra$barba
                                                    a$barbar
                                                    $barbara
```

The next step is to **sort these rotations lexicographically** (remember that the sentinel always comes before everything else). 

```
                                                    $barbara
                                                    a$barbar
                                                    ara$barb
                                                    arbara$b
                                                    bara$bar
                                                    barbara$
                                                    ra$barba
                                                    rbara$ba
```

Finally, we look at the **last column of the BWT matrix** to receive our BWT transform on "barbara\$": "arbbr$aa". That's it!

Notice $BWT(S)$ is a careful permutation of $S$. It will make $S$ much easier to compress (notice how a couple b's and a's are clustered together!). 

## BWT Decoding

So how do we get from $BWT(S)$ back to $S$- in other words, how to **decode** the BWT transformation? Not only is there always a defined way to recover $S$ from $BWT(S)$, but we can do so *efficiently*! Let's run through the process.

The first thing to note is that we can actually **reconstruct the BWT matrix from S**, one column at a time. Traditionally, we label the $BWT(S)$ as $L$ in the BWT matrix (for last column), and the first column as $F$. We can call the middle columns with whatever we want, but for simplicity we'll just call them by index.

                                                    F234567L
                                                    --------
                                                    $barbara
                                                    a$barbar
                                                    ara$barb
                                                    arbara$b
                                                    bara$bar
                                                    barbara$
                                                    ra$barba
                                                    rbara$ba
If you're observant, you'll figure that $F$ is simply just the characters in $S$ sorted lexicographically! We are, after all, sorting rotations lexicographically in the matrix, and each rotation begins with a single character of $S$. So we just sort $L$ to get $F$. Easy money.

Now remember that each row of our matrix was produced by a single character from the front (F) "wrapping around" to the back (L). That means that **each character in L is followed by the character in F in the same row**. 

Now here's the cool part. If we take pairs from the last and first columns and sort THOSE (LF), we actually get F2, and thus recover column 2. Try it yourself and convince yourself why this is the case!

Then, sorting LF2 gives us F23. Sorting LF23 gives us F234. And so on until we've recovered all of the matrix! We only needed ONE column to do all that, which is amazing! Once we recover the BWT matrix, decoding is simple: simply rotate ("wrap around") characters in *any* row until the sentinel reaches the end, or just find the row that ends in '\$'. 

This might seem like a lot of work, but in practice there's even *more* shortcuts, and **decoding can be done in $O(n)$ time** via a few *auxiliary* (extra) data structures to help us. 

That's for the next note!



