# Ask the user for a number and print its multiplication table

print("== Multiplication Table ==")
num = int(input("Enter a number: ")) # prompts the user to enter a number
# input() returns text and int() converts that text into an integer
# the resulting integer is stored in the variable num
for i in range(1, 11): # starts a loop whre i takes values from 1 through 10 inclusive
    print(f"{num} x {i} = {num * i}") # for each value of i prints a formatted line,  # it multiplies num by i and shows the result