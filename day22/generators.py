
def retrivedata():
    data=['1..100','101.200','201..300','301..400','401..500']
    for i in data:
        yield i
reels=retrivedata()
while True:  
    status=input('[s]croll or [q]uit:') 
    if status=='s':
        print(next(reels)) 
    else:
        break        


def even():
    i=0
    while True:
        i+=2
        yield i
n=10
result=even()
for i in range(n):
    print(next(result)) 



def factors(n):
    for i in range (1,n+1):
        if n%i==0:
           yield i
n=20
result=factors(n)
for i in result:
    print(i)     



def prime(n):
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i
n=10
res=prime(n) 
for i in res:
    print(i)               



'''
def countdown(n):
    data = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    for i in data:
        yield i
n = 10
result = countdown(n)
for i in result:
    print(i)    
'''