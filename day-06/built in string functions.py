Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # built in string functions
>>> a='shiva prasad'
>>> len(a)
12
>>> ord('p')
112
>>> ord('A')
65
>>> chr(65)
'A'
>>> min(a)
' '
>>> max(a)
'v'
>>> sorted(a)
[' ', 'a', 'a', 'a', 'd', 'h', 'i', 'p', 'r', 's', 's', 'v']
>>> # case conversion methods
>>> a='shiva prasad'
>>> a.upper()
'SHIVA PRASAD'
>>> a.capitalize()
'Shiva prasad'
>>> a.casefold()
'shiva prasad'
>>> a.lower()
'shiva prasad'
>>> a.swapcase()
'SHIVA PRASAD'
>>> a.title()
'Shiva Prasad'
>>> b='STRAẞEMÁLAGAÅngströmC'
>>> b.casefold()
'strassemálagaångströmc'
>>> a.center(50,'*")
...          
SyntaxError: incomplete input
>>> b.center(50,'*")
...          
SyntaxError: incomplete input
>>> b.center(50,'*')
         
'**************STRAẞEMÁLAGAÅngströmC***************'
a.center(60,'-')
         
'------------------------shiva prasad------------------------'
a.rjust(10,'-')
         
'shiva prasad'
a.rjust(50,'-')
         
'--------------------------------------shiva prasad'
'12'.zfill(4)
         
'0012'
# search and find metods
         
c='neenu mee chinna charan'
         
c.find('m')
         
6
c.rfind('e')
         
8
c.lfind('e')
         
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.lfind('e')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
c.index('e')
         
1
c.rindex('e')
         
8
c.count('e')
         
4
      # Replace and modify
         
d='virat kohli'
         
d.replace('i','1')
         
'v1rat kohl1'
c.replace('virat','shiva')
         
'neenu mee chinna charan'
d.replace('virat','shiva')
         
'shiva kohli'
d.maketrans('aeious','12345')
         
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d.maketrans('aeious','12345')
ValueError: the first two maketrans arguments must have equal length
d.maketrans('aeious','123456')
         
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53, 115: 54}
d.translate(d.maketrans('aeious','123456'))
         
'v3r1t k4hl3'
# spliting and joining methods
         
c.split()
         
['neenu', 'mee', 'chinna', 'charan']
'neenu', 'mee', 'chinna', 'charan'.split()
         
('neenu', 'mee', 'chinna', ['charan'])
'neenu', 'mee', 'chinna', 'charan'.split('-')
         
('neenu', 'mee', 'chinna', ['charan'])
'neenu', 'mee', 'chinna', 'charan'.split(',')
         
('neenu', 'mee', 'chinna', ['charan'])
s='''
python
programming
language'''
         
s.splitlines()
         
['', 'python', 'programming', 'language']
s.rsplit()
         
['python', 'programming', 'language']
s.join()
         
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s.join()
TypeError: str.join() takes exactly one argument (0 given)
'-'.join(['', 'python', 'programming', 'language'])
         
'-python-programming-language'
s.partition('-')
         
('\npython\nprogramming\nlanguage', '', '')
s.rpartition(',')
         
('', '', '\npython\nprogramming\nlanguage')
  # white space and trimming
         
s='               hello world       '
         
s.strip()
         
'hello world'
s.rstrip()
         
'               hello world'
l.strip()
         
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l.strip()
NameError: name 'l' is not defined
s.lstrip()
         
'hello world       '
  # encoding and decoding
         
text='hello shiva
         
SyntaxError: incomplete input
text='hello shiva'
         
text.encode()
         
b'hello shiva'

text.decode()
         
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
