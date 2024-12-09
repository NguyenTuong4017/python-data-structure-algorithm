
# Write a program that prints a dictionary 
# where the keys are numbers between 1 and N, and the values are square of keys.
n = int(input())

dict = {}

for i in range(1,n+1):
    dict.update({i:i*i})
    
print(dict)