res=[i for i in range(1,11)]
print(res)


n=12
res=[i for i in range(1,n+1) if n%i==0 ]
print(res)


r=[12,13,24,25,26,27,28,22,34,30,33]
res=[i if i%2==0 else 0 for i in r]
print(res)


r=[[12,23,45],[65,56,24],[34,43,57]]
res=[j for i in r for j in i if j%2==0]
print(res)


# if you want set comprehnsion add {} instead of this []
#ex:- [1,3,4] {1,2,3} to above programs
# set comprehnsion
res={i for i in range(1,11)}
print(res)


n=12
res={i for i in range(1,n+1) if n%i==0 }
print(res)


r=[12,13,24,25,26,27,28,22,34,30,33]
res={i if i%2==0 else 0 for i in r}
print(res)

'''
#synatx for condirions
l=[updating for loop]
l=[updating for loop if condition]
l=[update1 if condition update2 for loop]
l=[update for loop1 for loop2]
l=[update for loop1 for loop2 if cond]
'''

l=[int(input(f'Enter the number-{i+1}:')) for i in range(10)]
print(l)    


names=[input(f'enter the name-{i+1}:') for i in range (5)]




names={input(f'enter the name:{i+1}'): int(input('Enter the marks')) for i in range (5)}


res={i: i*i for  i in range (1,11)}
print(res)