Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,45]
... l=[10,9,6,1,2,3,4]
... l
... [10, 9, 6, 1, 2, 3, 4]
... id(1)
... 140724430178744
... i.append(12)
... Traceback (most recent call last):
...   File "<pyshell#4>", line 1, in <module>
...     i.append(12)
... NameError: name 'i' is not defined. Did you mean: 'id'?
... l.append(12)
... Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
... SyntaxError: invalid syntax
... l.append(14)
... l
... [10, 9, 6, 1, 2, 3, 4, 12, 14]
... id(1)
... 140724430178744
... l.append(6)
... l
... [10, 9, 6, 1, 2, 3, 4, 12, 14, 6]
... l.append(9)
... l
... [10, 9, 6, 1, 2, 3, 4, 12, 14, 6, 9]
... l.append(12, 7)
... Traceback (most recent call last):
...   File "<pyshell#14>", line 1, in <module>
...     l.append(12, 7)
... TypeError: list.append() takes exactly one argument (2 given)
... l
... [10, 9, 6, 1, 2, 3, 4, 12, 14, 6, 9]
... l.append(12,9)
... Traceback (most recent call last):
...   File "<pyshell#16>", line 1, in <module>
...     l.append(12,9)
... TypeError: list.append() takes exactly one argument (2 given)
... l
... [10, 9, 6, 1, 2, 3, 4, 12, 14, 6, 9]
... 

l[3]
1
id(1)
140724430178744
l[3]
1
l.pop()
9
l
[10, 9, 6, 1, 2, 3, 4, 12, 14, 6]
l.pop()
6
l.pop(1)
9
l
[10, 6, 1, 2, 3, 4, 12, 14]
l.clear()
l
[]
id(1)
140724430178744
l=[10,9,1,20,3,12,14]
l
[10, 9, 1, 20, 3, 12, 14]
max(1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    max(1)
TypeError: 'int' object is not iterable
max(l)
20
min(l)
1
sorred(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sorred(l)
NameError: name 'sorred' is not defined. Did you mean: 'sorted'?
sorted(l)
[1, 3, 9, 10, 12, 14, 20]
l
[10, 9, 1, 20, 3, 12, 14]
l.reverse()
l
[14, 12, 3, 20, 1, 9, 10]
l.sort()
l
[1, 3, 9, 10, 12, 14, 20]
l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
l.sort(reverse = True)
l
[20, 14, 12, 10, 9, 3, 1]
sum(1)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sum(1)
TypeError: 'int' object is not iterable
sum(l)
69
l = [1,2,3]
m = [1,2,3]
l
[1, 2, 3]
n = 1
n.append(4)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    n.append(4)
AttributeError: 'int' object has no attribute 'append'
n.append(4)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    n.append(4)
AttributeError: 'int' object has no attribute 'append'
n
1
l
[1, 2, 3]
m
[1, 2, 3]
m=l.copy()
m
[1, 2, 3]
m.append(10)
m
[1, 2, 3, 10]
l
[1, 2, 3]

all([0, '', [], (), set(),{},False])
False
all([1,'', [], (), set(),{},False])

False
SyntaxError: multiple statements found while compiling a single statement
any([1, '', [], (), set(),{},False])

False
SyntaxError: multiple statements found while compiling a single statement
l
[1, 2, 3]
l.index(3)
2
l
[1, 2, 3]
l.count(3)
1
l.count(4)
0
l.count(2)
1
l.count(5)
0
l
[1, 2, 3]
l=[[1,2,3] [4,5,6]]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    l=[[1,2,3] [4,5,6]]
TypeError: list indices must be integers or slices, not tuple
l=[[1,2,3],[4,5,6]]
l
[[1, 2, 3], [4, 5, 6]]
l(0)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    l(0)
TypeError: 'list' object is not callable
l[0]
[1, 2, 3]
l[1]
[4, 5, 6]
l[0],[2]
([1, 2, 3], [2])
l[-1,-1]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    l[-1,-1]
TypeError: list indices must be integers or slices, not tuple
l[-1][-1]
