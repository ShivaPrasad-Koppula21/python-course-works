'''
i=1
while i<=10:
print(i)
i+=1


i=10
while i>0:
    print(i)
    i-=1
'''
'''
i=2 
while i<=100:
    print(i,end=",")
    i+=2
'''    


'''
a='shiva prasad'
i=len(a)-1
while i>=0:
    print(a[i],end='')
    i-=1

'''
'''
# removing zero
l=[1,0,2,0,8,0,7,9,0,0,0,4,]
while 0 in l:
    l.remove(0)
print(l) 

'''
'''
# while loop using dict
data={}
total_bill=0
while True:
    product=input('enter the product( for exit)')
    if product=='exit':
        break
    price=int(input('enter the price'))
    total_bill+=price
    data[product]=price
print(data)   
print('total bill',total_bill)

'''
i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print('end of the loop')


# 8,9,11,14,17,18,20 leave questions