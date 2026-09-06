#multilevel inheritance
'''
class Whatsappv1:
    def messaging(self):
        print("you can message")
class Whatsappv2(Whatsappv1):
    def calls (self):
        print("you can make video and audio calls")
class Whatsappv3(Whatsappv2):
    def status(self) :
        print("you can add the status") 

a=Whatsappv1()
a.messaging() 

b=Whatsappv2()
b.messaging()
b.calls()

c=Whatsappv3()
c.messaging()
c.calls()
c.status()


#multiple inheritance
class Whatsappv1:
    def messaging(self):
        print("you can message")
class Whatsappv2:
    def calls (self):
        print("you can make video and audio calls")
class Whatsappv3(Whatsappv1,Whatsappv2):
    def status(self) :
        print("you can add the status") 

a=Whatsappv1()
a.messaging() 

b=Whatsappv2()
b.calls()

c=Whatsappv3()
c.messaging()
c.calls()
c.status()

# Heriachael inheritance 
class Whatsappv1:
    def messaging(self):
        print("you can message")
class Whatsappv2(Whatsappv1):
    def calls (self):
        print("you can make video and audio calls")
class Whatsappv3(Whatsappv1):
    def status(self) :
        print("you can add the status") 

a=Whatsappv1()
a.messaging() 

b=Whatsappv2()
b.messaging()
b.calls()

c=Whatsappv3()
c.messaging()
c.status()

# Hyberid inheritance

class Whatsappv1:
    def messaging(self):
        print("you can message")

class Whatsappv2:
    def extrameaasaging(self):
        print("you can add strickers and gifts")  

class Whatsappv3(Whatsappv1,Whatsappv2):
    def calls (self):
        print("you can make video and audio calls")

class Whatsappv4(Whatsappv3):
    def status(self) :
        print("you can add the status") 

a=Whatsappv1()
a.messaging() 

b=Whatsappv2()
b.extrameaasaging()

c=Whatsappv3()
c.messaging()
c.extrameaasaging()
c.calls()

d=Whatsappv4()
d.messaging()
d.extrameaasaging()
d.calls()
d.status()


# using super() class when we have same method use super
# we use this when ve have a single parent in child class 

class Whatsappv1:
    def status(self):
        print('you can add images and videos')
class Whatsappv2(Whatsappv1):
    def status(self):
        super().status()  # super()
        print("you can add music and stickers")  
class Whatsappv3(Whatsappv2):
    def status(self): 
        super().status()  #super()
        print("you can like and you can add reaction")
a=Whatsappv3() 
a.status()       
''' 

# for multiple parents
class Whatsappv1:
    def status(self):
        print('you can add images and videos')
class Whatsappv2(Whatsappv1):
    def status(self):
        print("you can add music and stickers")  
class Whatsappv3(Whatsappv1,Whatsappv2):
    def status(self): 
        Whatsappv1.status(self) 
        Whatsappv2.status(self) #super()
        print("you can like and you can add reaction")
a=Whatsappv3() 
a.status()       
        