Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,5,6,7}
s
{1, 2, 3, 4, 5, 6, 7}
a={1,2,3,4,5,6}
b={4,5,6,7,8,9,}
s={1,1,1,1,1,1}
s
{1}
a
{1, 2, 3, 4, 5, 6}
b
{4, 5, 6, 7, 8, 9}
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a&b
{4, 5, 6}
a-b
{1, 2, 3}
a^b  #symmetric difference
{1, 2, 3, 7, 8, 9}
a<=b #subset
False
a>=b #superset
False
{1,2,3,4,5,6,}<=a
True
5 in a
True
6 not in a
False
a.union (b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
{4, 5, 6}
a.issubset (b)
False
a.issuperset (b)
False
{1,2,3,4,5,6,} issubset (a)
SyntaxError: invalid syntax
a
{1, 2, 3, 4, 5, 6}
6 in a
True
      # set methods
      
max(a)
6
min(a)
1
sum(a)
21
a
{1, 2, 3, 4, 5, 6}
b=a
b
{1, 2, 3, 4, 5, 6}
b.add(8)
b
{1, 2, 3, 4, 5, 6, 8}
a
{1, 2, 3, 4, 5, 6, 8}
c=a.copy()
c.add(9)
a
{1, 2, 3, 4, 5, 6, 8}
c
{1, 2, 3, 4, 5, 6, 8, 9}
a
{1, 2, 3, 4, 5, 6, 8}
a.soretd()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.soretd()
AttributeError: 'set' object has no attribute 'soretd'
a.sorted
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.sorted
AttributeError: 'set' object has no attribute 'sorted'
a.discard(12)
a
{1, 2, 3, 4, 5, 6, 8}
a.add(11)
a
{1, 2, 3, 4, 5, 6, 8, 11}
a.update({11,12,13,14})
a
{1, 2, 3, 4, 5, 6, 8, 11, 12, 13, 14}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 6, 8, 11, 12, 13, 14}
a.remove(11)
a
{3, 4, 5, 6, 8, 12, 13, 14}
a.clear()
a
set()
a.update({3,4,5,})
a
{3, 4, 5}
a= frozenset({1,2,3,5,6,11,14,116})
a
frozenset({1, 2, 3, 5, 6, 11, 14, 116})
a.add(0)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.add(0)
AttributeError: 'frozenset' object has no attribute 'add'
    # DICTINORIES
    
d={}
d=dict()
type(d)
<class 'dict'>
d={'a':'1','b':'2','c':'3','d':'5'}
d
{'a': '1', 'b': '2', 'c': '3', 'd': '5'}
id(d)
2625612205056
d['e']='6'
d
{'a': '1', 'b': '2', 'c': '3', 'd': '5', 'e': '6'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d[2+3i]='complex'
SyntaxError: invalid decimal literal
>>> d[2+3j]='complex'
>>> d
{1: 'int', 12.3: 'float', (2+3j): 'complex'}
>>> d['str']='string'
>>> d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string'}
>>> d[(1,2,3,4)]='tiple'
>>> d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tiple'}
>>> d[9]='true'
>>> d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tiple', 9: 'true'}
>>> 9 in d
True
>>> 11 in d
False
>>> 'str' ind d
SyntaxError: invalid syntax
>>> 'str' in d
True
>>> d[(1,2,3,4)]
'tiple'
>>> 11 notin d
SyntaxError: invalid syntax
>>> d[12.3]
'float'
>>> d.get(1)
'int'
>>> d.get(10,'key is nor present')
'key is nor present'
>>> d.get(3,'key is not present')
'key is not present'
>>> d.get('str','key is jot present')
'string'
>>> d[12.3]=11.2
>>> d
{1: 'int', 12.3: 11.2, (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tiple', 9: 'true'}
>>> d['str']='shiva'
>>> d
{1: 'int', 12.3: 11.2, (2+3j): 'complex', 'str': 'shiva', (1, 2, 3, 4): 'tiple', 9: 'true'}
