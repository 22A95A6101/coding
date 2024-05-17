Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

====================================================== RESTART: C:/Users/durga/OneDrive/Desktop/Python/fun.py =====================================================
12
True

===================================================== RESTART: C:/Users/durga/OneDrive/Desktop/Python/fun1.py =====================================================
12 3
Traceback (most recent call last):
  File "C:/Users/durga/OneDrive/Desktop/Python/fun1.py", line 10, in <module>
    print(res)
NameError: name 'res' is not defined. Did you mean: 'res1'?

===================================================== RESTART: C:/Users/durga/OneDrive/Desktop/Python/fun1.py =====================================================
12 3
15

===================================================== RESTART: C:/Users/durga/OneDrive/Desktop/Python/fun1.py =====================================================
12 3
15
9
36
4.0
4
0
1728
add(2,3)
5

===================================================== RESTART: C:/Users/durga/OneDrive/Desktop/Python/fun1.py =====================================================
2 3
add: 5
-1
6
0.6666666666666666
0
2
8
>>> 
===================================================== RESTART: C:/Users/durga/OneDrive/Desktop/Python/fun1.py =====================================================
12 3
add: 15
sub: 9
mul: 36
div: 4.0
floordiv: 4
module: 0
power: 1728
>>> from math import *
>>> sqrt(2)
1.4142135623730951
>>> dir(math)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dir(math)
NameError: name 'math' is not defined
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
>>> import math as M
>>> m.floor(5.9977899)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    m.floor(5.9977899)
NameError: name 'm' is not defined. Did you mean: 'M'?
>>> M.floor(5.9977899)
5
