import re
email=input("enter the email:")
pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res=re.fullmatch(pattern,email)
print("valid email" if res else "invalid email")

phonenumber=input("enter the phone number:")
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
res=re.fullmatch(pattern,phonenumber)
print("valid phone number" if res else "invalid phone number")


password=input("enter the password")
pattern=r'^(?=.*[A-Z])(?=.*a-z)(?=.*\d)(?=.*[@$%*?&])[A-za-z\d@$%!%*?&]{8,}'
res=re.fullmatch(pattern,password)
print("valid password" if res else "invalid password")


username=input("enter the username:")
pattern=r"^[a-zA-Z][a-zA-Z0-9_]{2,19}$"
res=re.fullmatch(pattern,username)
print("valid username" if res else "invalid username")

aadhar 
pancard