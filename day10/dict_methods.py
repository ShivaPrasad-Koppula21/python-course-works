data={'name':'bunny','batch':63,'course':'PFS'}
data['name']
'bunny'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','bunny is not superstar')
'bunny is not superstar'
>>> data.get('course','bunny is not superstar')
'PFS'
>>> data['batch']=64
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS'}
>>> data['skills']=['python','mysql','flask']
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
>>> data['age']=21
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
>>> data.update({'phno':9032998114,'email':'koushik123@gmail.com'})
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9032998114, 'email': 'koushik123@gmail.com'}
>>> data.pop('age')
21
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9032998114, 'email': 'koushik123@gmail.com'}
>>> data.pop('phno')
9032998114
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com'}
>>> del data['name']
>>> data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com'}
>>> data.popitem()
('email', 'koushik123@gmail.com')
>>> data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
>>> data.popitem()
('skills', ['python', 'mysql', 'flask'])
>>> data
{'batch': 64, 'course': 'PFS'}
>>> data.clear()
>>> data
{}
>>> data.keys()
dict_keys([])
>>> data
{}
>>> data={'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com'}
>>> data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com'}
>>> data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'email'])
>>> data.values()
dict_values(['bunny', 64, 'PFS', ['python', 'mysql', 'flask'], 'koushik123@gmail.com'])
>>> data.items()
dict_items([('name', 'bunny'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('email', 'koushik123@gmail.com')])
>>> sorted(data)
['batch', 'course', 'email', 'name', 'skills']
sorted(data,reverse=True)
['skills', 'name', 'email', 'course', 'batch']
max(data)
'skills'
min(data)
'batch'
data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com'}
data['age']
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age')
data.setdefault('age',0)
0
data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com', 'age': 0}
data.setdefault('name','')
'bunny'
data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com', 'age': 0}
len(data)
6
all(data)
True
a
any(data)
True
data
{'name': 'bunny', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'koushik123@gmail.com', 'age': 0}
a={1:1,2:2}
b=a
b[3]=3
a
{1: 1, 2: 2, 3: 3}
b
{1: 1, 2: 2, 3: 3}
c=a.copy()
c[4]=4
c
{1: 1, 2: 2, 3: 3, 4: 4}
a
{1: 1, 2: 2, 3: 3}
d=dict.fromkeys(["a,"b"],0)
                 
SyntaxError: unterminated string literal (detected at line 1)
d=dict.fromkeys(["a,"b"],0)
                 
SyntaxError: unterminated string literal (detected at line 1)
d = dict.fromkeys(["a,"b"],0)
                   
SyntaxError: unterminated string literal (detected at line 1)
d=dict.fromkeys(["a","b"],0)
                   
d
                   
{'a': 0, 'b': 0}
