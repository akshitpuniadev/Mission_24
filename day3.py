# Day 3: The Calculator Logic & Data Types
# Mission: Phase 1 - Foundation Warrior

print("--- Welcome to Akki's Phase 1 Calculator ---")

# User se input lena aur use Number (int) mein badalna
num1 = int(input("Pehla Number dalo: "))
num2 = int(input("Dusra Number dalo: "))

# Saare Arithmetic Operations
print("Jod (Addition):", num1 + num2)
print("Ghatana (Subtraction):", num1 - num2)
print("Guna (Multiplication):", num1 * num2)
print("Bhag (Division):", num1 / num2)
print("Power (Exponential):", num1 ** num2)
print("Bacha hua (Remainder):", num1 % num2)

# Boolean Logic ka demo
print("\n--- Logic Check ---")
print(f"Kya {num1}, {num2} se bada hai?", num1 > num2)
