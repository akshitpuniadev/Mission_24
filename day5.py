# video-11: Strings Basics
name = "Harry"
friend = "Rohan"
apple = '''He said, 
Hi Harry
"I am good"'''

print("Hello, " + name)
# print(apple)

# Looping through a string
print("Characters in Harry:")
for character in name:
    print(character)

# video 12 : String Slicing
fruit = "Mango"
mangoLen = len(fruit)
print("Mango is a", mangoLen, "letter word.")

# Slicing Examples
print(fruit[0:4]) # Mang (0 index theke 3 porjonto)
print(fruit[1:4]) # ang
print(fruit[:5])  # Mango (shuru theke 4 index porjonto)
print(fruit[0:-3]) # Ma (len(fruit)-3 porjonto)

# Quick Quiz Answer for Day 12 (Example)
nm = "Harry"
# print(nm[-4:-2]) 
# Logic: nm[5-4 : 5-2] -> nm[1:3] -> Output: 'ar'
