# Profiling Python Code
[Profiling Tutorial, Python Timer functions](https://realpython.com/python-timer/#python-timer-functions)
```
~/Repos/code/COMMON/Exercises/highestN/python ❯❯❯  python -m cProfile -o report.out highestN.py

~/Repos/code/COMMON/Exercises/highestN/python ❯❯❯ python -m pstats report.out                                                                   [rc:1|h:3705]
Welcome to the profile statistics browser.
report.out%
report.out%
report.out%
report.out%
report.out% strip
report.out% sort cumtime
report.out% stats 10
Sun Oct 24 21:25:27 2021    report.out

         10631 function calls (10539 primitive calls) in 0.697 seconds

   Ordered by: cumulative time
   List reduced from 439 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.140    0.140    0.698    0.698 highestN.py:1(<module>)
        4    0.232    0.058    0.277    0.069 highestN.py:12(NLargestWithSet)
        4    0.000    0.000    0.190    0.048 highestN.py:8(NLargest)
        4    0.000    0.000    0.190    0.048 heapq.py:436(nlargest)
        4    0.190    0.048    0.190    0.048 {_heapq.nlargest}
        1    0.005    0.005    0.072    0.072 __init__.py:106(<module>)
        4    0.014    0.004    0.062    0.015 __init__.py:1(<module>)
        8    0.045    0.006    0.045    0.006 {sorted}
        1    0.001    0.001    0.042    0.042 add_newdocs.py:10(<module>)
        1    0.001    0.001    0.023    0.023 type_check.py:3(<module>)


report.out% ^D
Goodbye.
```