Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=''
s
''
>>> s='shiva'
>>> s
'shiva'
>>> 'shiva'+'prasad'
'shivaprasad'
>>> 'shivaprasad'*5
'shivaprasadshivaprasadshivaprasadshivaprasadshivaprasad'
>>> '-*-'*5
'-*--*--*--*--*-'
>>> s='shivaprasad'
>>> s[3]
'v'
>>> s[-5]
'r'
>>> names='shiva saicharan saivignesh chinnasimham'
>>> names[0]
's'
>>> names[-1]
'm'
>>> #s[start:end+1:step]=>[0:len:1]
>>> names[0:5]
'shiva'
>>> names[11:]
'aran saivignesh chinnasimham'
>>> names[-6:-13:-1]
'sannihc'
>>> names[::]
'shiva saicharan saivignesh chinnasimham'
>>> names[::1]
'shiva saicharan saivignesh chinnasimham'
>>> shiva in names
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    shiva in names
NameError: name 'shiva' is not defined
>>> shiva in names
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    shiva in names
NameError: name 'shiva' is not defined
