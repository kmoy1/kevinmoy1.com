# HMMs

HMMs are widely used in speech recognition. A recording is split into *frames* of 10-20 ms, which are then *quantized* into some predefined categories. Then given that sequence of categories, we find out what (English) that sequence represents. 

We can do the same thing in sequencing. Given a protein sequence, for example, what protein family does it belong to? Note there can be "noise" in these sequences (e.g. indels) but we have to be resistant to that!

## CpG islands

The **dinucleotide** CpG (cytosine, guanine) frequently occurs in the human genome. There's a high chance of C mutating to T, though, which makes CpG significantly rarer. **CpG islands** are variable-sized regions in the genome where many more CpG nucleotides exist than elsewhere. 