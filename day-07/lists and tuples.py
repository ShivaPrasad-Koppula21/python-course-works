Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c='siva prasad'
c.startswith('si')
True
c.endswith("ad")
True
c.startwith('as')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c.startwith('as')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
c.startswith('as')
False
c.isupper()
False
c.islower()
True
"PYTHON".is upper()
SyntaxError: invalid syntax
>>> "PYTHON".isupper()
True
>>> 's1234'.isalnum()
True
>>> 's.1234'.isalnum()
False
>>> 'this is apple'.istitle()
False
>>> 'This Is Apple'.istitle()
True
>>> 'shiva'.isidentifier()
True
>>> 'sh@iva'.isidentifier()
False
>>>   # LISTS  AND TUPLES
...   
>>> l=[1,2,3,4,5,6,(1,2,3),{6,7,8,9},{1:2,2:4,3:5}]
>>> l=type()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l=type()
TypeError: type() takes 1 or 3 arguments
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7,8]
>>> l+m
[1, 2, 3, 4, 5, 6, 7, 8]
>>> m*3
[5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8]
>>> l[2]
3
>>> l[:2]
[1, 2]
>>> l[2:]
[3, 4]
>>> l[::-1]
[4, 3, 2, 1]
>>> 2 isin l()
SyntaxError: invalid syntax
