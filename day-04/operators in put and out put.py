
a= 20
b=5
a+b
25
a-b
15
a*b
100
a**b
3200000
a/b
4.0
a//b
4
a%b
0
# comparsion opertor
a=10
b=20
a>=b
False
a=b
a<=b
True
a<b
False
a>b
False
a==b
True
a!=b
False
# assignment opertaror
a=10
a+=20
c
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c
NameError: name 'c' is not defined
a
30
c-=5
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c-=5
NameError: name 'c' is not defined
c
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c
NameError: name 'c' is not defined
a-=5
c
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c
NameError: name 'c' is not defined
a
25
a*=2
a
50
a**=2
a
2500
# relation operator
a=10
a%2==0
True
a%3==0
False
a%2==0 and a%3==0
False
a%2==0 or a%3==0
True
a<5
False
not a<5
True
# str list tuple set dict
a='shiva'
'a' in a
True
'b'not in a
True
'k' in a
False
'a' not in a
False
l=[1,2,3,4,5,]
4 in l
True
7 not in l
True
7 in l
False
a={'name' : 'shiva' 'course' :63,}
SyntaxError: invalid syntax
a={'name' : 'shiva' 'course' 'king'}
'shiva' in a
False
'name'in a
True
63 in a
False
# identity operator
a=(1,2,3,4,)
b=(1,2,3,4)
id(a)
2272631904736
id(b)
2272633172544
a is b
False
c=b
b=a
id (b)
2272631904736
a in c
False
c in b
False
a=10
id (a)
2272595673616
s={1,2,3,4}
id(s)
2272633096224
s.add (6)
s
{1, 2, 3, 4, 6}
id (s)
2272633096224
# bit wise operator
# bit wise operator
9&10
8
9|10
11
9^10
3
8>>2
2
8<<2
32
>>> # output formation
>>> a=10
>>> b=10.3
>>> c='shva'
>>> print(a,b,c)
10 10.3 shva
>>> print('a value is',a)
a value is 10
>>> print('a value is' ,a,'|b value is" ,b,' | c value is',c)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print (f'a={a} b={b} c={c}')
...       
a=10 b=10.3 c=shva
>>> a=10 b=10.3 c=shva
...       
SyntaxError: invalid syntax
>>> 
>>> SyntaxError: invalid syntax
...       
SyntaxError: incomplete input
>>> 
>>> print('a ={} | b= {} | c={}'.format(a,b,c))
...       
a =10 | b= 10.3 | c=shva
>>> a =10 | b= 10.3 | c=shva
...       
SyntaxError: cannot assign to expression
>>> print('a ={} | b= {} | c={}'.format(c,b,a))
...       
a =shva | b= 10.3 | c=10
>>> print('a ={} | b= {2} | c={0}'.format(c,b,a))
...       
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print('a ={} | b= {2} | c={0}'.format(c,b,a))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> print('a ={1} | b= {2} | c={0}'.format(c,b,a))
...       
a =10.3 | b= 10 | c=shva
