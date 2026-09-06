def display(n):
    n=n+10
    print('inside:',n)
n=10
display(n)  
print('outside:',n) 



def display():
    print('inside:',n)
n=10
display()
print('outside:',n)


def display():
    global n
    n=n+10
    print('inside',n)
n=10
display()
print('outside',n)


def display():
    global n
    n='pfs'
    print('updated course:',n)
n='jfs'
display()
print('final course:',n)


def display():
    n='jfs'
    def update():
        nonlocal n
        n='pfs'
        print('updated course:',n)
        update()
        print('final course:',n)
display()    



