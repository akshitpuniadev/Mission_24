# ==========================================
# PART 1: FOR LOOPS (Day 17)
# ==========================================
# For loop tab use hota hai jab humein pata ho ki kitni baar loop chalana hai.

# String par loop chalana
name = "Akshit"
print("Iterating over a string:")
for i in name:
    print(i)

# List par loop chalana
colors = ["Red", "Green", "Blue", "Yellow"]
print("\nIterating over a list:")
for color in colors:
    print(color)
    # Nested loop: Har color ke characters par loop
    for i in color:
        print(i)

# Range function ka use (0 se 4 tak chalega)
print("\nUsing range(5):")
for k in range(5):
    print(k + 1) # 1 se 5 tak print karega

# Range with Step (Start, Stop, Step)
# 1 se shuru, 12 tak (11 tak jayega), aur 3-3 ka gap
print("\nRange with Step (1, 12, 3):")
for i in range(1, 12, 3):
    print(i)


# ==========================================
# PART 2: WHILE LOOPS (Day 18)
# ==========================================
# While loop tab tak chalta hai jab tak condition 'True' rehti hai.

# Basic While Loop
i = 0
print("\nBasic While Loop (0 to 2):")
while(i < 3):
    print(i)
    i = i + 1  # Increment karna zaroori hai warna loop infinite ho jayega

# Decrementing While Loop (Ulta Loop)
count = 5
print("\nDecrementing Loop:")
while (count > 0):
    print(count)
    count = count - 1

# While Loop with Else
# Jab loop ki condition 'False' ho jati hai, tab else wala part chalta hai.
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print("Loop ki condition khatam, main else ke andar hoon!")

# ==========================================
# PART 3: DO-WHILE EMULATION (Bonus)
# ==========================================
# Python mein direct 'do-while' nahi hota, par hum aise kar sakte hain:
print("\nEmulating Do-While (Runs at least once):")
while True:
    number = int(input("Enter a positive number (0 to quit): "))
    print(number)
    if not (number > 0):
        break  # Loop se bahar nikalne ke liye
