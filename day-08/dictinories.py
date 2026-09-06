
data={'name':'shiva','age':21,'course':'python'}
data
{'name': 'shiva', 'age': 21, 'course': 'python'}
data['name']
'shiva'
21 in data
False
data.get{'age','key is not present'}
SyntaxError: invalid syntax
data.get('age','key is not present')
               
21
data.pop('age')
         
21
data
         
{'name': 'shiva', 'course': 'python'}
data={'name':'shiva','age':21,'course':'python','email':'shiva@gmail.com','phno':123456,'batch':63,}
         
data
         
{'name': 'shiva', 'age': 21, 'course': 'python', 'email': 'shiva@gmail.com', 'phno': 123456, 'batch': 63}
data.keys()
         
dict_keys(['name', 'age', 'course', 'email', 'phno', 'batch'])
data.values()
         
dict_values(['shiva', 21, 'python', 'shiva@gmail.com', 123456, 63])
data.items()
         
dict_items([('name', 'shiva'), ('age', 21), ('course', 'python'), ('email', 'shiva@gmail.com'), ('phno', 123456), ('batch', 63)])
sorted(data)
         
['age', 'batch', 'course', 'email', 'name', 'phno']
sorted(data,reverse=True)
...          
['phno', 'name', 'email', 'course', 'batch', 'age']
>>> ['age', 'batch', 'course', 'email', 'name', 'phno']
...          
['age', 'batch', 'course', 'email', 'name', 'phno']
>>> max(data)
...          
'phno'
>>> min(data)
...          
'age'
>>> data
...          
{'name': 'shiva', 'age': 21, 'course': 'python', 'email': 'shiva@gmail.com', 'phno': 123456, 'batch': 63}
>>> data('age')
...          
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data('age')
TypeError: 'dict' object is not callable
>>> data['age']
...          
21
>>> data.get('age')
...          
21
>>> data.setdefault('age',22)
...          
21
>>> data
...          
{'name': 'shiva', 'age': 21, 'course': 'python', 'email': 'shiva@gmail.com', 'phno': 123456, 'batch': 63}
>>> len(data)
...          
6
>>> all(data)
...          
True
>>> any (data)
...          
True
