# ==========================================
# BREAK AND CONTINUE STATEMENTS (Day 19)
# ==========================================
# Inka use hum loops (for/while) ke normal flow ko badalne ke liye karte hain.

# 1. BREAK STATEMENT
# Iska matlab hai: "Bas bahut hua, ab loop se bahar nikal jao!"
print("--- Example of BREAK ---")
for i in range(1, 13):
    if(i == 10):
        print("10 aagaya, ab ruk jao!")
        break # Loop yahin khatam ho jayega, 11 aur 12 print nahi honge
    print("5 x", i, "=", 5 * i)

print("Loop ke bahar aagaye!")


# 2. CONTINUE STATEMENT
# Iska matlab hai: "Is wali bari (iteration) ko skip karo aur agli par jao."
print("\n--- Example of CONTINUE ---")
for i in range(1, 13):
    if(i == 10):
        print("Skip kar rahe hain 10 ko...")
        continue # 10 wala print skip ho jayega, par loop 11 aur 12 ke liye chalega
    print("5 x", i, "=", 5 * i)


# 3. WHILE LOOP MEIN BREAK (Emulating Do-While)
# Jaisa Harry sir ne bataya, hum infinite while loop ko break se control kar sakte hain.
print("\n--- While Loop with Break ---")
i = 0
while True:
    print(i)
    i = i + 1
    if(i % 10 == 0):
        break # Jaise hi i 10 ka multiple hoga, loop ruk jayega


# 4. QUICK QUIZ (Day 19)
# Ek aisa loop jo user se input le aur tab tak chalta rahe jab tak user 0 na dabaye.
"""
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    print("Aapne enter kiya:", num)
"""
