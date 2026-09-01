d={}
>>> d=dict()
>>> type(d)
<class 'dict'>
>>> d={'kl':'v1','k2':'v2','k3':'v3'}
>>> d
{'kl': 'v1', 'k2': 'v2', 'k3': 'v3'}
>>> id(d)
2259632276800
>>> d['k4']='v4'
>>> d
{'kl': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
>>> id(d)
2259632276800
>>> d['k5']='v11'
>>> d
{'kl': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v11'}
>>> d={}
>>> d[1]='int'
>>> d
{1: 'int'}
>>> d[12.3]='float'
>>> d
{1: 'int', 12.3: 'float'}
>>> d[2+4j]='complex'
>>> d
{1: 'int', 12.3: 'float', (2+4j): 'complex'}
>>> d['str']='string'
>>> d
{1: 'int', 12.3: 'float', (2+4j): 'complex', 'str': 'string'}
>>> d[(1,2,3]='tuple'
...   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> d[(1,2,3)]='tuple'
...   
>>> d
...   
{1: 'int', 12.3: 'float', (2+4j): 'complex', 'str': 'string', (1, 2, 3): 'tuple'}
>>> d[False]='False'
...   
>>> d
...   
{1: 'int', 12.3: 'float', (2+4j): 'complex', 'str': 'string', (1, 2, 3): 'tuple', False: 'False'}
>>> d[frozenset({1,2,4})]='fset'
...   
>>> d
...   
{1: 'int', 12.3: 'float', (2+4j): 'complex', 'str': 'string', (1, 2, 3): 'tuple', False: 'False', frozenset({1, 2, 4}): 'fset'}
>>> d={}
...   
>>> d[1]=1
  
d[2]=12.3
  
d[3]=12+4j
  
d[4]='str'
  
d[5]=[1,2,3,4]
  
d[6]=(1,2,3)
  
d[7]={1,2,3}
  
d[8]={1:1}
  
d[9]=True
  
d
  
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
#operations
  
9 in d
  
True
10 in d
  
False
'str' in d
  
False
d[5]
  
[1, 2, 3, 4]
d[8]
  
{1: 1}
d[10]
  
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d[10]
KeyError: 10
d.get(10)
  
d.get(1)
  
1
d.get(10,"bunny is not superstar")
  
'bunny is not superstar'
d.get(6,"bunny is not superstar")
  
(1, 2, 3)
d[3]=4
  
d
  
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
d[5]=10
  
d
  
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
d[6]=13
  
d
  
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 13, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
d[9]=34
  
d
  
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 13, 7: {1, 2, 3}, 8: {1: 1}, 9: 34}
