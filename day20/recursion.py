'''

def display(n):
    if n>15:
        return
    print(n)
    display(n+1)
display(1) 


def display(n):
    if n>15:
        return
    display(n+1)
    print(n)
display(1) 


def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(9))



def productof(n):
    if n==1:
        return 1
    return n*productof(n-1)
print(productof(4))



def fun(ind):
    if ind==len(s):
        return
    print(s[ind])
    fun(ind+1)
s="shviva prasad"
fun(0)

a="python"  ip
p    op
py
pyt
pyth
pytho
python 

def fun(a):
    if a>len(s):
        return
    print(s[:a])
    fun(a+1)
s="shiva"
fun(1)

'''

def display(index,width):
    if index>len(s):
        return
    print(s[index:index+width])
    display(index+1,width)
s="python programming"
display(0,10) 



def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)
n=987654
display(n)    

