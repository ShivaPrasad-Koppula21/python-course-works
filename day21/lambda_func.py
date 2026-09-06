grater=lambda a,b:a if a>b else b
print(grater(11,32))
print(grater(12,23))
print(grater(11,45))

wish=lambda name:f'welcome to the course {name}'
print(wish('shiva'))
print(wish('sai'))
print(wish('sunny'))

iseven=lambda n:'even' if n%2==0 else 'odd'
print(iseven(24))
print(iseven(20))
print(iseven(33))


domain=lambda mail:(mail.split('@')[-1].split('.')[0])
print(domain('shiva@gmail.com'))
print(domain('shiva@codegnan.com'))
print(domain('shiva@yahoo.com'))
print(domain('shiva@xyzzzzzz.com'))

gst=lambda price: price + price*0.18
print(gst(20000))
print(gst(10000))
print(gst(30000))


# USING MAP FUNNCTIONS
prices=[340,543,123,243,333]
result=list(map(lambda price:price*0.18,prices))
print(result)

names=['shiva','saicharan','saivignesh','sunny']
result=list(map(lambda name:name.title(),names))
print(result)

price=[100,200,300,400]
result=list(map(lambda price: price-price*0.3,price))
print(result)

# Filter function
price=[100,200,49,400]
result=list(filter(lambda price: price>50,price))
print(result)

price=[100,200,400,33]
result=list(filter(lambda price: price%2==0,price))
print(result)

price=[100,200,49,400]
result=list(filter(lambda price: price%2!=0,price))
print(result)


names={'shiva','sai','hai','virat','kohli'}
result=list(filter(lambda name:len(name)>3,names))
print(result)


from functools import reduce
l=[4,55,6,788,65,45]
res=reduce(lambda sum,i:sum+i,l)
print(res)

names=['shiva','virat','kohli']
res=reduce(lambda res,i: res+i,names)
print(res)


names=['shiva','virat','kohli']
res=reduce(lambda res,i: res+' '+i,names)
print(res)


#sorted

products={'sugar':60,'salt':50,'bread':70,'oil':108}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),key=lambda i:i[1])))