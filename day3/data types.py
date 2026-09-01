
type(count)
<class 'int'>
price=10.9
type(count)
<class 'int'>
price=99.9
type(price)
<class 'float'>
c=3+8i
SyntaxError: invalid decimal literal
c=3+8j
c=3+8i
SyntaxError: invalid decimal literal

c=3+8j
type(c)
<class 'complex'>
s='shiva'"shiva"
tpy(s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tpy(s)
NameError: name 'tpy' is not defined
s='shiva'
tpye(s)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tpye(s)
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
s="shiva"
type(s)
<class 'str'>
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4,4,5,'fgdfhk'68.67,[1,43,5,5],(2,3,3,)]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l=[1,2,3,4,4,5,'fgdfhk',68.67,[1,43,5,5],(2,3,3,)]
>>> l
[1, 2, 3, 4, 4, 5, 'fgdfhk', 68.67, [1, 43, 5, 5], (2, 3, 3)]
 type(l)
<class 'list'>
 s
'shiva'

NameError: name 'g' is not defined
>>> s={}
>>> s={1,2,3,4,4,}
>>> s=()
>>> type(s)
<class 'tuple'>
>>> ststus=none
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    ststus=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status=none
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    status=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status= none
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    status= none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status=None
>>> type(status)
<class 'NoneType'>
>>> s={1,2,3,4,5,5,}
>>> s.remove(3)
>>> s
{1, 2, 4, 5}
>>> s=frozenset({1,2,4,4,})
>>> s
frozenset({1, 2, 4})
