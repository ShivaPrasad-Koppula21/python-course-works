'''
s='python programming'
for  i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
       print(i,s[i])
       '''
'''
l=[1,2,22,34,55,66,43,55,77,88,28]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+1
        print(i,l[i])
print(sum)
'''

'''
a=int(input("enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(f'factorial of {a} is {fact}')  
'''
'''
data = {}
n = int(input("Enter the no of students:"))
max_marks = 0
for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    if marks > max_marks:
        max_marks = marks
        data[name] = marks
        print(data)
        print("Maximum Marks:",max_marks)
        '''

'''
n = int(input("Enter the no of products: "))
total_bill = 0
products = {}
for i in range(n):
   product = input(f"Product - {i}: ")
   price =float(input(f"Price- {i}: "))
   quantity = int(input(f"Quantity -{i}: "))
   final_price = price*quantity
   total_bill += final_price
   products[product] = f'{price} * {quantity} = {final_price}'
   print(products)
   print("Total Bill:",total_bill)
   '''



