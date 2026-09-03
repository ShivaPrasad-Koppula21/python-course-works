'''
for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print('end of the loop')  
'''
'''
pin=12345
for _ in range(3):
    epin=int(input('enter the pin'))
    if pin==epin:
        print('unlock the phone')
        break
    else:
        print('invalid pin') 
else:
    print('try after 30 seconds')  

'''
'''
# factors of numbers
n=int(input('enter the number'))
print('factors:,'end=' ')
for i in range(1,n+1):
    if n%i==0:
     print(i,end=' ')

     '''
'''
# prime numbers
n=int(input ('enter the number '))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print('prime number')
else:
    print('not a prime number')  

'''


n=int(input('enter the number'))
for i in range(2,n//2+1):
    if n%i==0:
        print('not a prime number')
        break
else:
    print(' prime  number')   

   