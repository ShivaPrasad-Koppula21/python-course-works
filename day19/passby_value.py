'''
# int float str list tuple set dict bool
# int float str tuple bool
#list set dict 



def display(n):
    n[5]=6
    print('inside:',n)
n={1:2,3:4}
display(n) 
print('outside:',n)  

''' 

a=int(input('enter the units'))
senior=int(input('enter senior or not')).lower()=='senior'
if a<0 or 100:
    print(a*4)
elif a>101 or 200:
    print(a*2.5) 
elif a>201 and 500:
        print(a*4) 
else:
   print(a*6)      
