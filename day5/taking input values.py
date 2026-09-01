Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
... charan
... a
... 'charan'
... name=input()
... nani
... name
... 'nani'
... age=input("enter the age: ")
... enter the age: 21
... 
... age
... '21'
... 
... type(age)
... <class 'str'>
... 
... names=input("Enter the names: ")
... Enter the names: sai charan 
... names
... 'sai charan '
... names.split()
... ['sai', 'charan']
... names=input("enter the names: ").split()
... enter the names: sai charan
... names
... ['sai', 'charan']
... names=input("enter the names: ").split()
... enter the names: 1 2 3 4 5 6
... names
... ['1', '2', '3', '4', '5', '6']
... list(map(int,names))
... [1, 2, 3, 4, 5, 6]
... values=list(map(int,input().split()))
... 1 2 3 4 4 5 55 66
... values
... [1, 2, 3, 4, 4, 5, 55, 66]
... values=list(map(float,input().split()))
... 1 2 3 4 4 5 55 66
... values
[1.0, 2.0, 3.0, 4.0, 4.0, 5.0, 55.0, 66.0]
[1.0, 2.0, 3.0, 4.0, 4.0, 5.0, 55.0, 66.0]
[1.0, 2.0, 3.0, 4.0, 4.0, 5.0, 55.0, 66.0]
names =tuple(input("Enter the names: ").split())
Enter the names: shiva charan nani
names
('shiva', 'charan', 'nani')
SyntaxError: multiple statements found while compiling a single statement
values= set(map(int,input().split()))
values
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    values= set(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'values'
# multipe inputs
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
emial, password=input("enter the email and password:").split())
SyntaxError: unmatched ')'
emial, password=input("enter the email and password:").split()))
SyntaxError: unmatched ')'
emial, password=input("enter the email and password:").split()
enter the email and password:shiva 123456
emial
'shiva'
password
'123456'
a,b,c=list(map(int,input().split()

 a,b,c=list(map(int,input().split()))
               
SyntaxError: '(' was never closed
a,b,c=list(map(int,input().split()))
               

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 0)
ValueError: not enough values to unpack (expected 3, got 0)
               
SyntaxError: invalid syntax
e=eval(input())
               
e
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'e' is not defined
1
               
1
e
               
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    e
NameError: name 'e' is not defined
