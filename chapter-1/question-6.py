# Write a program that sums all of the numbers taken as input, while ignoring any input that is not a valid number.
# Your program should display the current sum after each number is entered. 
# It should display an error message after each non-numeric input, and then continue to sum any additional numbers entered by the user.  The program exits when the user enters 0. 
# Ensure that your program works correctly for both integers and floating-point numbers.


n = input()
sum = 0
while (n != "0"):
    try:
        num = float(n)
        sum += num
        print("The total is now", sum)
    except ValueError:
        print("That wasn’t a number.")
        
    n = input()
    
print("The grand total is", sum)    
