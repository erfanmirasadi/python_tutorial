print("part 3 :")

 # CS101 Lab-03
# Your Student-ID Name Surname
# Department

def collatz_sequence(n):
    max_number = n
    print(f"Please enter a number: {n}")
    
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        max_number = max(max_number, n)
    
    print(1)  # Printing 1 at the end of the sequence
    return max_number

# Input from user
number = int(input("Enter a number: "))

# Part-3 Collatz sequence
max_number = collatz_sequence(number)
print(f"\nThe maximum number you get is: {max_number}")