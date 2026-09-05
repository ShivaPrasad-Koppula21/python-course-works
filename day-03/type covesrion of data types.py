
a=20
str(a)
'20'
float(a)
20.0
list(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> comple(A)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    comple(A)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(a)
(20+0j)
>>> bool(a)
True
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> 
>>> int
<class 'int'>
>>> float
<class 'float'>
>>> complex
<class 'complex'>
>>> list
<class 'list'>
>>> tuple
<class 'tuple'>
>>> set
<class 'set'>
>>> dict
<class 'dict'>
>>> bool
<class 'bool'>
