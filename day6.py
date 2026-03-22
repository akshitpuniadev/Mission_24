# ==========================================
# VIDEO 1: STRING METHODS (Day 13)
# ==========================================

name = "  Harry Harry !!!  "

# 1. upper() - Sab capital letters mein badalne ke liye
print(name.upper()) 

# 2. lower() - Sab chhote (small) letters mein badalne ke liye
print(name.lower()) 

# 3. rstrip() - String ke aakhiri characters (jaise !!!) hatane ke liye
print(name.rstrip("!")) 

# 4. replace() - Ek word ko dusre word se badalne ke liye
print(name.replace("Harry", "John")) 

# 5. split() - String ko tod kar List banane ke liye (space se todega)
print(name.split(" ")) 

# 6. capitalize() - Sirf pehla letter bada karne ke liye
blog = "intro to python"
print(blog.capitalize()) 

# 7. center() - String ko beech mein lane ke liye (50 space ke beech mein)
print(blog.center(50)) 

# 8. count() - Ginne ke liye ki 'Harry' kitni baar aaya hai
print(name.count("Harry")) 

# 9. endswith() aur startswith() - Check karne ke liye ki shuru/khatam kispe ho raha
print(name.endswith("!!!")) 
print(name.startswith("  Harry"))

# 10. find() - Word ki position (index) dhundne ke liye
print(name.find("Harry")) # Agar nahi mila toh -1 dega

# 11. index() - find() jaisa hi hai par agar nahi mila toh ERROR dega
# print(name.index("Zayn")) # Yeh error dega kyunki Zayn nahi hai

# 12. Boolean checks (True ya False)
msg = "Welcome007"
print(msg.isalnum())  # Kya sirf letters aur numbers hain? (True)
print(msg.isalpha())  # Kya sirf letters hain? (False, kyunki 007 numbers hain)
print(msg.islower())  # Kya sab chhote letters hain?
print(msg.isprintable()) # Kya screen par dikhne layak hai? (\n printable nahi hota)
print(msg.isspace())   # Kya sirf space hai?
print(msg.istitle())   # Kya har word ka pehla letter Capital hai?

# 13. swapcase() - Bade ko chhota aur chhote ko bada karne ke liye
print(name.swapcase())

# 14. title() - Puri string ko Title format mein badalne ke liye
print("his name is dan".title())


# ==========================================
# VIDEO 2: IF-ELSE CONDITIONALS (Day 14)
# ==========================================

# 1. int(input()) - User se number lene ke liye (Typecasting)
age = int(input("Apni age likho: "))

# 2. Basic If-Else logic
# Yaad rakhein: ':' lagana aur print ko thoda aage (Indentation) likhna zaroori hai
if(age > 18):
    print("Aap drive kar sakte hain")
else:
    print("Abhi aap chhote hain, drive nahi kar sakte")

# 3. Elif Ladder - Jab 2 se zyada conditions ho
price = 210
budget = 200

if (price <= budget):
    print("Apple khareed lo")
elif (price - budget <= 50):
    print("Thoda mehenga hai par chalo le lo")
else:
    print("Bahut mehenga hai, rehne do")

# 4. Nested If-Else - If ke andar ek aur If
num = 18
if (num < 0):
    print("Number negative hai")
elif (num > 0):
    if (num <= 10):
        print("Number 1 se 10 ke beech hai")
    elif (num > 10 and num <= 20):
        print("Number 11 se 20 ke beech hai")
    else:
        print("Number 20 se bada hai")
else:
    print("Number zero hai")
