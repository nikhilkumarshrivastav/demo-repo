# Function to calculate the sum of even numbers between 1 and 100
def sum_even_numbers():
    total = 0
    for num in range(1, 101):
        if num % 2 == 0:
            total += num
    return total

# Call the function and print the result
result = sum_even_numbers()
print(f"The sum of all even numbers between 1 and 100 is: {result}")
