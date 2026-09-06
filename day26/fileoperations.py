# to open a file
file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

# to read a file
''''
with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())


# to write a file
with open('new_file','w') as file:
    file.write('you can write here')

# to append  something
with open('pfs-63.txt','a') as file:
    file.write('you can add to previous one')

#read + write
with open ('pfs-63.txt','a+') as file:
    file.write("you can read and write")
    file.seek(0)
    print(file.read())

'''
