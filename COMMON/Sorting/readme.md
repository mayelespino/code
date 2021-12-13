# Common exercises

## Sorting

I created a few versions of the merge sort algorithm, I think this algorithm is well suited to implement multi threaded because the approach of divide and conquer. There is no overlap in the memory usage and little to no need to lock and/or syncronize.

When running on a multi core machine, each thread is a nicely isolated and encaspsulated unit of work. This approach should be a lot faster than the single threaded version, by a factor equal to the number of cores.

I found it to be an interesting exercise, with some surprises. For example on the same machine, Python starts having a few issues when the number of threads is above 999, it errors out. Instead Go can do 9999 like it is nothing, it starts to struggle at 999999, but still completes.

----
and starts to struggle at 999999, but still completes.