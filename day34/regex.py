#match using(check only pattern)
import re
pattern = r'[0-9]'
text = 'codegnan'
res = re.match(pattern,text)
print(res.group()if res else "pattern not found")

#search(check  whole entire string)
pattern = r'[0-9]'
text = 'codegnan2026'
res = re.search(pattern,text)
print(res.group()if res else "pattern not found")

#findall(list of pattern it gives)
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'
res = re.findall(pattern,text)
print(res)

#finditer(it is also give index)
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
    
#print(res)

#fullmatch(what only needded thing)
pattern = r'[0-9]{10}'
text = '6302760173'
res = re.fullmatch(pattern,text)

#split use when you more than one character to split
pattern=r'[,(#]'
text='python,java(html#css'
res=re.split(pattern,text)
print(res)

#sub is used to replace
pattern=r'[a-z]'
text='shiva 2002, happy-17'
res=re.sub(pattern,'*',text)
print(res)


#.is use to we can replace any thing with . 
pattern=r'e.t'
text='e@t eat,eaat,eet ett ect wertt trre '
res=re.findall(pattern,text)
print(res)

# ^ is used to check first starts with
pattern=r'^(91)'
text='91987654432 '
res=re.findall(pattern,text)
print(res)

#$ uesd to check ends with
pattern=r'2$'
text='91987654432'
res=re.findall(pattern,text)
print(res)

# +  is used to one or more occurance
pattern=r'to+'
text='to toffhf tffff too tooo t tooooo'
res=re.findall(pattern,text)
print(res)

# * is used to 
pattern=r'ab*'
text='ab abbb a abbbbb abbbb'
res=re.findall(pattern,text)
print(res)

# | used for this or that
pattern=r'91|0'
text='01234'
res=re.findall(pattern,text)
print(res)

# [] to find 
pattern=r'[aeiouAEIOU]'
text='shivaoo prausad'
res=re.findall(pattern,text)
print(res)
