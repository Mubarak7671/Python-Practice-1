#String : String is collection of charecters 
# Written in '' " " """ """/''' ''' 
# String is used for Names, emails ,passwords,messages etc... 

#text ="Hello"
#text[0]="h"
#print(text) #show error

str1="I am python" 
str2="Python is very interesting"
print(type (str1))
print(str2) 
 #positive indexing - left to right 
 #negative indexing - right to left  
 #slice:[start:stop:step] {slice : group of charecters}
text1 = "My Name is Shaik Mubarak"
print(text1[0::1])# Normal String
print(text1[::-1])# Reverce the string
print(text1[-9::3]) 

#case conversion
text3 ="Python Program 2026"
print(text3.upper())
print(text3.lower())
print(text3.title())
print(text3.capitalize())
print(text3.swapcase())
print(text3.casefold())  
# Example :- 
saved_username = "shaik"
user_input = input("Enter username: ")
if user_input.lower() == saved_username.lower():
    print("Login Successful")
else:
    print("Invalid Username")
 
# Search Methods :-  
text4="Hello ,Welcome to Python programming . Python is awesome" 
#find () & rfind() -1
#index() & rindex() value error
print (text4.find("mubbu")) #-1
print (text4.find("programming")) #25 
print (text4.index("is"))
#print (text4.index("call")) # value error
print (text4.rfind("python",20)) 
# Count method :-
print (text4.count("Python")) #2 times
print (text4.count("o"))# 7 Times 
# Starswith & Endswith() method:- 
email ="shaikmubarak@234gmail.com"
print(email.startswith("shaik")) 
file ="document.pdf"
print(file.endswith(("pdf")))
# Validation Method :- 
name1 = "Shaik" #(isalpha)
print(name1.isalpha()) #true
name2="Mubbu123"
print(name2.isalpha()) #false
#2.isdigit 
num ="Hello143"
print (num.isdigit()) #False
num2="123"
print (num2.isdigit())#true 
#3.alnum
email1="shaik143" #conatain Alphabets+numbers
print(email1.isalnum()) 
#4.space  only spaces
space=" "
print(space.isspace()) 

def validate_password(password):

    if len(password) < 8:
        return "At least 8 characters required"
    if not any(c.isupper() for c in password):
        return "Please include at least one uppercase character"
    if not any(c.islower() for c in password):
        return "Please include at least one lowercase character"
    if not any(c.isdigit() for c in password):
        return "Please include at least one digit"
    return "Password is valid"
print(validate_password("Passone")) 
# Modification methods :- 
# replace:- 
t = "I like Java"
print(t.replace("Java", "Python"))
#strip:-# rstrip & lstrip
k="  Hello   "
print(k.rstrip())
# ============================================
# STRING MASTER PROJECT - ALL CONCEPTS COVERED
# Author: Shaik Practice File
# ============================================
print("\n========== STRING PROJECT START ==========\n")
# --------------------------------------------
# 1. STRING CREATION
# --------------------------------------------
print("1. STRING CREATION")
str1 = "Python"
str2 = 'Programming'
str3 = """Strings are very important"""
print(str1)
print(str2)
print(str3)
# --------------------------------------------
# 2. STRING IMMUTABILITY
# --------------------------------------------
print("\n2. STRING IMMUTABILITY")
name = "Shaik"
print("Original:", name)
# Strings cannot be changed directly
# name[0] = "M" ❌ Error
name = "Mubarak"  # ✅ New string created
print("Updated:", name)
# --------------------------------------------
# 3. INDEXING
# --------------------------------------------
print("\n3. INDEXING")
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])
# --------------------------------------------
# 4. SLICING
# --------------------------------------------
print("\n4. SLICING")
sentence = "Python Programming"
print("Slice [0:6]:", sentence[0:6])
print("Slice [7:]:", sentence[7:])
print("Reverse:", sentence[::-1])
# --------------------------------------------
# 5. STRING CONCATENATION
# --------------------------------------------
print("\n5. CONCATENATION")
first = "Shaik"
last = "Ahmed"
full_name = first + " " + last
print("Full Name:", full_name)
# --------------------------------------------
# 6. CASE CONVERSION METHODS
# --------------------------------------------
print("\n6. CASE CONVERSION")
msg = "welcome to python"
print("Upper:", msg.upper())
print("Lower:", msg.lower())
print("Title:", msg.title())
print("Capitalize:", msg.capitalize())
print("Swapcase:", msg.swapcase())
# --------------------------------------------
# 7. SEARCH METHODS
# --------------------------------------------
print("\n7. SEARCH METHODS")
data = "Python is easy and Python is powerful"
print("find('Python'):", data.find("Python"))
print("rfind('Python'):", data.rfind("Python"))
print("count('Python'):", data.count("Python"))
print("startswith('Python'):", data.startswith("Python"))
print("endswith('powerful'):", data.endswith("powerful"))
print("'easy' in string:", "easy" in data)
# --------------------------------------------
# 8. MODIFICATION METHODS
# --------------------------------------------
print("\n8. MODIFICATION METHODS")
text2 = "   I like Java   "
print("Original:", text2)
print("Strip:", text2.strip())
print("Replace Java->Python:", text2.replace("Java", "Python"))
words = "apple,banana,mango"
print("Split:", words.split(","))
items = ["Laptop", "Mobile", "Camera"]
print("Join:", " | ".join(items))
# --------------------------------------------
# 9. VALIDATION METHODS
# --------------------------------------------
print("\n9. VALIDATION METHODS")
username = "Shaik123"
otp = "987654"
space = "   "
print("isalpha:", "Shaik".isalpha())
print("isdigit:", otp.isdigit())
print("isalnum:", username.isalnum())
print("isspace:", space.isspace())
print("islower:", "python".islower())
print("isupper:", "PYTHON".isupper())
# --------------------------------------------
# 10. STRING FORMATTING METHODS
# --------------------------------------------
print("\n10. FORMATTING METHODS")
product = "Laptop"
price = 55000
qty = 2
total = price * qty
# f-string formatting
print(f"Product: {product}")
print(f"Price: ₹{price}")
print(f"Quantity: {qty}")
print(f"Total Bill: ₹{total}")
# Decimal formatting
value = 123.4567
print(f"Formatted Value: {value:.2f}")
# --------------------------------------------
# 11. MINI PROJECTS (REAL WORLD USE)
# --------------------------------------------
print("\n========== MINI PROJECTS ==========")
# Mini Project 1: Email Username Extractor
print("\nMini Project 1: Username from Email")
email = "shaik@gmail.com"
username = email[:email.index("@")]
print("Email:", email)
print("Username:", username)
# Mini Project 2: Phone Number Masking
print("\nMini Project 2: Phone Masking")
phone = "9876543210"
masked_phone = phone[:2] + "******" + phone[-2:]
print("Original:", phone)
print("Masked:", masked_phone)
# Mini Project 3: Password Validator
print("\nMini Project 3: Password Validation")
def validate_password(password):
    if len(password) < 8:
        return "At least 8 characters required"
    if not any(c.isupper() for c in password):
        return "Include at least one uppercase letter"
    if not any(c.islower() for c in password):
        return "Include at least one lowercase letter"
    if not any(c.isdigit() for c in password):
        return "Include at least one digit"
    return "Password is Valid ✅"
print(validate_password("Pass1234"))
# Mini Project 4: Product Search Feature
print("\nMini Project 4: Product Search")
products = ["Laptop", "Mobile", "Headphones", "Camera"]
search = "mobile"
for item in products:
    if search.lower() in item.lower():
        print("Found Product:", item)
print("\n========== STRING PROJECT END ==========\n")










