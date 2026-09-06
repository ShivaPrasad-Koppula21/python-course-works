'''

def shiva(name,email,password):    #define once call whenever needed
    print(f'hello:{name}')
    print(f'your email:{email}')
    print(f'your password:{password}')
shiva('virat','shiva@gmail.com', '1223345')    
shiva('shiva','shiva@gmail.com', '1223345')    
shiva('prasad','shiva@gmail.com', '1223345') 



def isleapyear(year):
    if year%400==0 or(year%4==0 and year%100!=0):
        print(f'{year} is leap year')
    else:
        print(f'{year} not a leap year')
for year in range(2000,2027):
    isleapyear(year)        



def sumofdigits(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum
n=int(input('enter the numbers'))
print(f'sum of {n} digits is {sumofdigits(n)}')  

 


def productofdigits(n):
    pro=1
    while n>0:
        pro*=n%10
        n=n//10
    return pro
n=int(input('enter the numbers'))
print(f'product {n} digits is {productofdigits(n)}')  

'''  


# strong password or wak password
def checkpassword(password):
    if len(password)>8:
        check=set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check)==4:
            return "strong password" 
    return("weak password") 
password=input("enter the password") 
print(f'{checkpassword(password)}')             

        