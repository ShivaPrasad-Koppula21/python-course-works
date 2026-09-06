#positional arguments
''''
def shiva(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
shiva('virat','virat@gmail.com','12345')   
shiva('kohli@gmail.com','122345','kohli') 
shiva('1234','shiva','shiva@gmail.com')


# key word arguments
def shiva(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
shiva(name='virat',email='virat@gmail.com',password='12345')   
shiva(email='kohli@gmail.com',password='122345',name='kohli') 
shiva(password='1234',name='shiva',email='shiva@gmail.com')


#  default arguments
def shiva(name,email='',password=''):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
shiva(name='virat',email='virat@gmail.com',password='12345')   
shiva(email='kohli@gmail.com',name='kohli') 
shiva(password='1234',name='shiva',)

'''
#VARABLE LENGTH ARGUMENT positional
def display(*names):
       print(names)
display('shiva')
display('shiva','sai',)
display('shiva','sai','sunny')       


#VARABLE LENGTH ARGUMENT keyword
def display(**products):
    print(products)
display(bag=6000)
display(bag=6000,book=300)
display(bag=6000,book=300,bottle=4000)