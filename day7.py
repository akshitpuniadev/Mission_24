# ==========================================
# VIDEO 1: EXERCISE 2 - GOOD MORNING SIR (Day 15)
# ==========================================
# Isme humne 'time' module aur 'if-elif-else' ka use kiya hai

import time

# Current time nikalne ke liye strftime ka use hota hai
timestamp = time.strftime('%H:%M:%S')
print("Current Time:", timestamp)

# Sirf ghante (Hour) nikal kar use Integer mein badalna zaroori hai
# Kyunki comparison hamesha numbers ke beech hota hai, text ke beech nahi
hour = int(time.strftime('%H'))

# Greeting Logic
if (hour >= 0 and hour < 12):
    print("Good Morning Sir!")
elif (hour >= 12 and hour < 17):
    print("Good Afternoon Sir!")
elif (hour >= 17 and hour < 21):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")


# ==========================================
# VIDEO 2: MATCH CASE STATEMENTS (Day 16)
# ==========================================
# Ye Python 3.10+ mein aaya hai aur switch-case ki tarah kaam karta hai

x = int(input("Enter a number: "))

# Match case mein indentation (space) ka khaas dhyan rakhein
match x:
    # Agar x ki value 0 hai
    case 0:
        print("x is zero")
    
    # Agar x ki value 4 hai
    case 4:
        print("case is 4")
    
    # Hum conditions (if) bhi laga sakte hain case ke andar
    case _ if x < 10:
        print("x is less than 10")
        
    # Default case: Jab upar ka kuch bhi match na ho (Underscore '_' use karein)
    case _:
        print("No specific match found for:", x)

# ==========================================
# EXTRA TIP: STRFTIME FORMATS
# ==========================================
# %H - Hours (24-hour format)
# %M - Minutes
# %S - Seconds
# %d - Day
# %m - Month
# %Y - Year
