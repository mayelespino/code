# Python research and interview questions

- Can lists have a mix of types?
yes
- Can arrays have a mix of types?
yes
- Are tuples more efficient than lists?
```
Lists are allocated in two blocks: the fixed one with all the Python object information and a variable sized block for the data. It is the reason creating a tuple is faster than List. It also explains the slight difference in indexing speed is faster than lists, because in tuples for indexing it follows fewer pointers.

In python we have two types of objects. 1. Mutable,  2. Immutable. In python lists comes under mutable objects and tuples comes under immutable objects.

Tuples are stored in a single block of memory. Tuples are immutalbe so, It doesn't require extraspace to store new objects.
Lists are allocated in two blocks: the fixed one with all the Python object information and a variable sized block for the data.
It is the reason creating a tuple is faster than List.
It also explains the slight difference in indexing speed is faster than lists, because in tuples for indexing it follows fewer pointers.
Advantages using tuples:
Tuples is that they use less memory where lists use more memory
We can use tuples in a dictionary as a key but it's not possible with lists
We can access element with an index in both tuples and lists
Disadvantages of tuples
We cannot add an element to tuple but we can add element to list.
We can't sort a tuple but in a list we can sort by calling "list.sort()" method.
We can't remove an element in tuple but in list we can remove element
We can't replace an element in tuple but you can in a list
Reference:

https://docs.python.org/2/library/functions.html#tuple
```
https://learnbatta.com/blog/why-tuple-is-faster-than-list-in-python-22/

- which are the immutable types?
```
Immutable Objects : These are of in-built types like int, float, bool, string, unicode, tuple. In simple words, an immutable object can’t be changed after it is created.
```
https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/


