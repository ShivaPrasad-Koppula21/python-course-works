from abc import ABC, abstractmethod
class phonepay(ABC):
    def  senderinfo(self):
        print("you can enter their mobile number or qr")
    def amount(self):
        print('you can enter amount') 
    def pin(self):
        print('you need to enter the pin')  
    @abstractmethod
    def transaction(self):
        pass

class SBI(phonepay):
    def transaction(self):
        print('payment using sbi')
class HDFC(phonepay):
    def transaction(self):
        print('payment using hdfc')
class BOB(phonepay):
    def transaction(self):
        print('payment using bob')  

shiva=SBI()
shiva.senderinfo()
shiva.amount()
shiva.pin()
shiva.transaction()

sai=HDFC()
sai.senderinfo()
sai.amount()
sai.pin()
sai.transaction()


