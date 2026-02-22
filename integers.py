# =============================TO -DO'S=======================
# Write code to reverse an integer (e.g., 123 → 321, -123 → -321, handle overflow if any)

def reverse_integers():
    number = int(input("Enter the number: "))
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0
    while number != 0:
        digit = number%10
        reversed_number = reversed_number*10 +digit
        number //= 10
    reversed_number *= sign
    print(f"the reversed number is : {reversed_number}")
    
reverse_integers()    
# Check if an integer is palindrome without converting to string.
def is_palindrome():
     number = int(input("Enter the number: "))
     if number < 0 :
         return False
     given_number = number
     palindrome = 0
     while number !=0:
         digit = number % 10
         palindrome = palindrome*10 + digit
         number //=10
     return given_number == palindrome
if is_palindrome():
    print(f"The number is palindrome",)
else :
    print("not a palindrome")         
# Find the sum of all digits in an integer.
def sum_of_digits(number):
    total = 0
    number = abs(number)
    while number>0:
        total =total+number %10
        number //= 10
    return total
print(sum_of_digits(12345))    
# Implement a function to check if a number is prime.
def is_prime():
    number = int (input ("Enter the number: "))
    for i in range(2,number):
        if number % i == 0:
            print("It's not a prime number")
            break
    else:
         print("It is a prime number")        
is_prime()        
# Calculate factorial of n iteratively and recursively.
def factorial():
    number = int(input("Enter the number: "))
    fact =1
    for num in range(1,number+1):
        fact =fact*num
    print(f"factorial of number is : {fact}")
    
factorial()    
    
# Find GCD of two integers using Euclidean algorithm.
# Convert integer to binary string manually (no bin()).
# Count set bits (1s) in binary representation.
# Implement pow(x, n) efficiently (binary exponentiation).
# Find the single number in an array where others appear twice (XOR).
def single_number(numbers):
    result = 0
    for number in numbers:
        result ^= number
    return result

result = single_number(numbers = [12,1,12,2,4])
print(result)

