''' 
for i in range(5): # i is outer loop  used for rows
    for j in range(10): # j is inner loop usedfor column
        print('*',end=' ')
    print()   



for i in range(5):
    for j in range (5):
        print('*',end=" ")
    print()    
 

for row in range (5):
    for column in range(5):
        print(row,end=' ')
    print()  


for i in range(5):
    for j in range(5):
        print(i+j,end=' ') 
    print()            

for i in range (5):
    for j in range(5):
        print(j%2,end=" ")
    print()  


for i in range (5):
    for j in range (5):
        print((i+j)%2,end=' ') 
    print()  

for i in range (5):
    print('*'*(i+1)) 
'''
'''
for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()  
'''     
for i in range(5):
    print('*'*(5-i))
