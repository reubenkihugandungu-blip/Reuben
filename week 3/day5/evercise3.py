# Use a list comprehension to get all even numbers from 1 to 30

evens = [n for n in range(1, 31) if n % 2 == 0]
print(evens)

# Now get the squares of those even numbers
squares = [n**2 for n in evens]
print(squares)