The Python heapq module also defines two more operations:

    heapreplace() is equivalent to heappop() followed by heappush().
    heappushpop() is equivalent to heappush() followed by heappop().

These are useful in some algorithms since they’re more efficient than doing the two operations separately.

element 0 is always the smallest

heaps are implemented as complete binary trees

Since priority queues are so often used to merge sorted sequences, the Python heapq module has a ready-made function, merge(), for using heaps to merge several iterables. merge() assumes its input iterables are already sorted and returns an iterator, not a list.

If I only need the lowest value, instead of sorting can I not just do O(n) comparison until I find the lowest?
Maybe find the 2nd lowest too?
Insertion sort but without the O(n) check?

Perhaps a generator expression?

Heaps can also help identify the top n or bottom n things. The Python heapq module has high-level functions that implement this behavior.

For example, this code gets as input the times from the women’s 100 meters final at the 2016 Summer Olympics and prints the medalists, or top three finishers:


