# sorting_tree
Create and store code for sorting trees of various lengths.
Sorting trees are the fastest sorting algorithms out there when it comes to time complexity & space complexity.

The currect fastest non-paralell sorting algorith is TimSort with a complexity of n log(n).
A sorting tree is of time complexity log(n!)

To put things in perspective for n = 10
TimSort makes approximately 40 comparisons where as a sorting tree will make only 22. TimSort also has various other overheads needed for looping, where as in sorting tree the only operation is a simple comparison with no overheads.

The objective of this project is to create sorting trees for length upto n = 10, for larger sorting trees the code size will excete 1GB so the objective will be to write code to use smaller trees to generate larger sorting trees.



