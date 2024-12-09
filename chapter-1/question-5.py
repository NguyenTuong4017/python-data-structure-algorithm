# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

vowel = ['a','e','o','u','i']

s = input()

count = 0

for char in s:
    if char.lower() in vowel:
        count += 1
        
print("Number of vowels:",count)

