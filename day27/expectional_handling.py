'''
try:
    a=int(input(''))
except ValueError:
    print('enter a correct number dayatype')
else:
    print('a=',a)
finally:
    print("end of the program")
'''

try:
    k={1:2,3:4} 
    l=[12,22] 
except (ValueError,KeyError, IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print('Error occured:',e)  
else:
    print("Error free program")
finally:
    print('End of the program')
'''    
except KeyError:
    print('key is not there') 
except IndexError:
    print('index out of range')
except ZeroDivisionError:
    print('cant divide with zero')  
except TypeError:
    print('enter the correct data  type')   
except NameError:
    print('enter the correct program')                  
'''    
try:
    # a=int(input('enter:'))
    k={1:2,3:4} 
    #print(k[13])
    l=[12,22] 
    #print(10/10)
except Exception as e:
    print('Error occured:',e)  
else:
    print("Error free program")
finally:
    print('End of the program')


try:
    amount=int(input('enter the amount:'))
    balance=5000
    raise Exception ('amount needs to de positive')
except Exception as e:
    print('error occured:',e)
else:
    print('error free program')
finally:
    print('end of the program')    

try:
    amount=int(input('enter the amount:'))
    balance=5000
    if amount<0:
      raise Exception ('amount needs to de positive')
except Exception as e:
    print('error occured:',e)
else:
    print('error free program')
finally:
    print('end of the program')          