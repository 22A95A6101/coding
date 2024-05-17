Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data=[10,20,30,40,50,60,70,80]
>>> data
[10, 20, 30, 40, 50, 60, 70, 80]
>>> data[0]
10
>>> data[-1]
80
>>> data[3:5:1]
[40, 50]
>>> data[4:6:-1]
[]
>>> data[4:1:-1]
[50, 40, 30]
>>> len(data)
8
>>> sum(data)
360
>>> max(data)
80
>>> min(min)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    min(min)
TypeError: 'builtin_function_or_method' object is not iterable
>>> min(data)
10
>>> data.append(90)
>>> data
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> data.insert(3,40)
>>> data
[10, 20, 30, 40, 40, 50, 60, 70, 80, 90]
>>> a=[10,20,30]
>>> b=[40,50,60]
>>> a.extends(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.extends(b)
AttributeError: 'list' object has no attribute 'extends'. Did you mean: 'extend'?
a.extend(b)
a
[10, 20, 30, 40, 50, 60]
data.pop()
90
data.pop(3)
40
